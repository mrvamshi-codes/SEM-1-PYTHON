#learning json.loads() -- converted the json string into python dictionary

import json

json_str = '{"Name":"Vamshi","Age":18,"Branch":"CSE"}'

data = json.loads(json_str)

print(data)
print(type(data))