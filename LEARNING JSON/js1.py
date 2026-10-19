import json

data={
    "name":"Vamshi",
    "Age":18,
    "Branch":"CSE"
}

json_str = json.dumps(data)

print(json_str)
print(type(json_str))