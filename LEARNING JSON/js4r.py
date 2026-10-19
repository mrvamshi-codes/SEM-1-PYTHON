#reading from a json file

import json

with open("student.json","r") as f:
    data=json.load(f)

print(data)
print(type(data))