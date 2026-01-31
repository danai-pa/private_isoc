import requests

print("STEP 1: Call CKAN package_show API")

api_url = "https://catalog-dga.data.go.th/th/api/3/action/package_show"
params = {"id": "9443ffaa-8aa0-4922-93e5-a8c2374eb8d8"}

data = requests.get(api_url, params=params, timeout=60).json()

print("success =", data.get("success"))

result = data.get("result", {})
print (type(result))
for k , v in result.items():
    print(k,":",v)
# resources = result.get("resources", [])
# print("resources =", type(resources))
# print("dataset_name =", result.get("name"))
# print("dataset_title =", result.get("title"))
# print("num_resources =", result.get("num_resources"))

# # ดู key ทั้งหมดของ result (ช่วยให้เข้าใจโครงสร้าง)
# print("result_keys_sample =", list(result.keys())[:20])
