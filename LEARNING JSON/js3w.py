#wrtiting JSON to a file

import json

data = {
    "name":"Vamshi",
    "Age":18,
    "Branch":"CSE"
}

with open("student.json","w") as f:
    json.dump(data,f)

print("Data written successfully")