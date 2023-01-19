import json

with open("Question.json", 'r') as file:
    data = json.load(file)

i=0
for field in data:
    data[i]["number"] = i
    i += 1

with open("Unique.json", "w") as reversed:
    json.dump(data, reversed)


