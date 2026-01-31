"""
Generate SQLAlchemy (Declarative) models from existing database tables.

Run examples:
  python3 -m generators.gen_models_cli --db-key test --schema public
  python3 -m generators.gen_models_cli --db-key test --schema public --tables users,orders
  python3 -m generators.gen_models_cli --db-key test --schema public --output generators/output/models.py --overwrite
"""

import argparse
import os
from typing import Any, Dict, List, Optional, Set, Tuple

from sqlalchemy import inspect  # type: ignore
from sqlalchemy import Column, ForeignKey, text  # type: ignore
from sqlalchemy import (
    Integer, BigInteger, SmallInteger,
    String, Text,
    Boolean,
    Float, Numeric,
    Date, DateTime, Time,
    LargeBinary,
)  # type: ignore

try:
    # SQLAlchemy 1.4+
    from sqlalchemy.orm import declarative_base  # type: ignore
except Exception:  # pragma: no cover
    from sqlalchemy.ext.declarative import declarative_base  # type: ignore

from database.engine import get_engine

Base = declarative_base()


# ---------- helpers ----------
def _safe_ident(name: str) -> str:
    """Make a class name from table name: my_table -> MyTable"""
    parts = [p for p in name.replace("-", "_").split("_") if p]
    return "".join([p[:1].upper() + p[1:] for p in parts]) or "Model"

def _py_str(s: str) -> str:
    """Python string literal with safe escaping."""
    return repr(s)

def _render_type(coltype: Any, used: Set[str]) -> str:
    """
    Render SQLAlchemy type to code string.
    Covers common types; falls back to repr(type) string.
    """
    # String-like with length
    if isinstance(coltype, String):
        used.add("String")
        length = getattr(coltype, "length", None)
        return f"String({length})" if length else "String()"

    if isinstance(coltype, Text):
        used.add("Text")
        return "Text()"

    if isinstance(coltype, (Integer, BigInteger, SmallInteger)):
        tname = coltype.__class__.__name__
        used.add(tname)
        return f"{tname}()"

    if isinstance(coltype, Boolean):
        used.add("Boolean")
        return "Boolean()"

    if isinstance(coltype, Float):
        used.add("Float")
        return "Float()"

    if isinstance(coltype, Numeric):
        used.add("Numeric")
        precision = getattr(coltype, "precision", None)
        scale = getattr(coltype, "scale", None)
        if precision is not None and scale is not None:
            return f"Numeric(precision={precision}, scale={scale})"
        if precision is not None:
            return f"Numeric(precision={precision})"
        return "Numeric()"

    if isinstance(coltype, DateTime):
        used.add("DateTime")
        tz = getattr(coltype, "timezone", None)
        return "DateTime(timezone=True)" if tz else "DateTime()"

    if isinstance(coltype, Date):
        used.add("Date")
        return "Date()"

    if isinstance(coltype, Time):
        used.add("Time")
        return "Time()"

    if isinstance(coltype, LargeBinary):
        used.add("LargeBinary")
        return "LargeBinary()"

    # Fallback
    # Many dialect-specific types repr nicely (e.g. VARCHAR(length=255))
    # We'll emit it as a string inside "text" is wrong; so fallback to generic String().
    used.add("String")
    return "String()"


def _collect_fks(inspector: Any, table: str, schema: Optional[str]) -> Dict[str, str]:
    """
    Return mapping: column_name -> ForeignKey("schema.table.col") code
    """
    fks = inspector.get_foreign_keys(table, schema=schema)
    out: Dict[str, str] = {}
    for fk in fks or []:
        constrained_cols = fk.get("constrained_columns") or []
        referred_table = fk.get("referred_table")
        referred_cols = fk.get("referred_columns") or []
        referred_schema = fk.get("referred_schema") or schema

        if not (referred_table and constrained_cols and referred_cols):
            continue

        for ccol, rcol in zip(constrained_cols, referred_cols):
            if referred_schema:
                target = f"{referred_schema}.{referred_table}.{rcol}"
            else:
                target = f"{referred_table}.{rcol}"
            out[ccol] = f'ForeignKey({_py_str(target)})'
    return out


def generate_models_code(
    db_key: str,
    schema: Optional[str] = "public",
    tables: Optional[List[str]] = None,
) -> str:
    """
    Generate python code string containing SQLAlchemy Declarative models.
    """
    engine = get_engine(db_key)
    inspector = inspect(engine)

    if tables is None or len(tables) == 0:
        tables = inspector.get_table_names(schema=schema)

    used_types: Set[str] = set()
    lines: List[str] = []

    # Header
    lines.append("# Auto-generated SQLAlchemy models")
    lines.append("# DO NOT EDIT MANUALLY")
    lines.append("")
    lines.append("from sqlalchemy import Column, ForeignKey, text")
    lines.append("from sqlalchemy import Integer, BigInteger, SmallInteger, String, Text, Boolean, Float, Numeric, Date, DateTime, Time, LargeBinary")
    lines.append("try:")
    lines.append("    from sqlalchemy.orm import declarative_base")
    lines.append("except Exception:  # pragma: no cover")
    lines.append("    from sqlalchemy.ext.declarative import declarative_base")
    lines.append("")
    lines.append("Base = declarative_base()")
    lines.append("")

    for table in tables:
        class_name = _safe_ident(table)

        pk = inspector.get_pk_constraint(table, schema=schema) or {}
        pk_cols = set(pk.get("constrained_columns") or [])

        fk_map = _collect_fks(inspector, table, schema)

        cols = inspector.get_columns(table, schema=schema) or []

        lines.append(f"class {class_name}(Base):")
        lines.append(f"    __tablename__ = {_py_str(table)}")

        if schema:
            lines.append(f"    __table_args__ = {{'schema': {_py_str(schema)}}}")

        if not cols:
            lines.append("    # (No columns found)")
            lines.append("    pass")
            lines.append("")
            continue

        for col in cols:
            col_name = col["name"]
            coltype = col["type"]
            nullable = bool(col.get("nullable", True))

            type_code = _render_type(coltype, used_types)

            args: List[str] = [type_code]
            # FK?
            if col_name in fk_map:
                args.append(fk_map[col_name])

            kwargs: List[str] = []
            if col_name in pk_cols:
                kwargs.append("primary_key=True")
            if not nullable:
                kwargs.append("nullable=False")

            # server default (best-effort)
            default = col.get("default", None)
            if default is not None:
                # Keep it as text("...") to avoid executing
                kwargs.append(f"server_default=text({_py_str(str(default))})")

            args_join = ", ".join(args + kwargs)
            lines.append(f"    {col_name} = Column({args_join})")

        lines.append("")

    return "\n".join(lines)


def write_models_file(code: str, output_path: str, overwrite: bool = False) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if os.path.exists(output_path) and not overwrite:
        raise FileExistsError(f"File exists: {output_path} (use --overwrite)")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db-key", required=True, help="key passed to get_engine(db_key)")
    ap.add_argument("--schema", default="public", help="schema name (use empty for none)")
    ap.add_argument("--tables", default="", help="comma-separated table list; empty = all tables")
    ap.add_argument("--output", default="generators/output/models.py", help="output python file path")
    ap.add_argument("--overwrite", action="store_true", help="overwrite output file if exists")
    args = ap.parse_args()

    schema = args.schema.strip()
    if schema == "" or schema.lower() == "none":
        schema = None

    tables = [t.strip() for t in args.tables.split(",") if t.strip()] if args.tables else None

    code = generate_models_code(db_key=args.db_key, schema=schema, tables=tables)
    write_models_file(code, args.output, overwrite=args.overwrite)
    print(f"✅ Generated models -> {args.output}")


if __name__ == "__main__":
    main()
