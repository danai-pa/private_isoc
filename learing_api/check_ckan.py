import requests

BASE = 'https://opendata.ddc.moph.go.th'
# r = requests.get(f'{BASE}/api/3/action/package_list', timeout=30)
# print("status:", r.status_code)
# print("content-type:", r.headers.get("content-type"))
# print("content-text:", r.text[:200])


dataset_id = "doed-01"

r = requests.get(
    f"{BASE}/api/3/action/package_show",
    params={"id": dataset_id},
    timeout=30
)
print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
d = r.json()
# print("success:" , d.get("success"))
result = d.get("result", {})
print("title:", result.get("title"))
resources = result.get("resources", [])
# resources = {}
# print("resources type:", type(resources))
want = {"csv", "xls", "xlsx"}
for i , v in enumerate(resources):
    name=(v.get("name") or "").strip().lower()
    fmt=(v.get("format") or "").strip().lower() 
    url=(v.get("url") or "").strip().lower()
    print(f"{i} name",': ',name)
    print(f"{i} fmt",': ',fmt)
    print(f"{i} url",': ',url)

    if not url:
        print("no url")
        continue
    
    is_match = False
    if fmt in want:
        is_match = True
        print("fmt", fmt)
    else:
        for w in want:
            if w in url:
                is_match = True
                print("w", w)
    # print("is_match:", is_match)



