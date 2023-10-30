import json

with open("atmlocations.txt", "r") as f:
    data = f.read()

atmdic = json.loads(data)

print(atmdic)
print(atmdic['serviceDetails']['serviceDetls'][32])
