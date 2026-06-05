import json

json_data = """{
  "name": "Ivan",
  "age": 32,
  "is_student": true,
  "courses": ["Python", "QA auto", 32],
  "address": {
    "city": "Moscow",
    "zip": 1
  }
}"""
parsed_data = json.loads(json_data)

print(parsed_data["courses"], type(parsed_data))


data = {
    'name': 'Мария',
    'age': 25,
    'is_student': True
}

json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(data, type (data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)