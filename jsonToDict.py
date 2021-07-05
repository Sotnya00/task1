import json

with open('students.json', 'r+', encoding = 'utf=8') as student:
    data = json.load(student)
print(data)

with open('rooms.json', 'r+', encoding='utf-8') as rooms:
    data1 = json.load(rooms)
print(data1)