import json

data = {'people': [{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}

# PRINT DIRECT TO FILE
with open('data.json', 'w') as f:
    json.dump(data, f)
    # f.write(data)

# PRINT WITH NEWLINE CHARACTERS
with open('data2.json', 'w') as f2:
    jstr = json.dumps(data, indent=4)
    json.dump(json.dumps(data, ensure_ascii=False, indent=4), f2)

# PRINT PRETTY PRINTED
with open('data3.json', 'w') as f3:
    f3.write(json.dumps(data, indent=4))

print(json.dumps(data, indent=4))
