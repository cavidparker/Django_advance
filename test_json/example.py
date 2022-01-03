import json
f = open('example.json')
data = json.load(f)
print(data['education'][0]['Institude name'])
f.close()