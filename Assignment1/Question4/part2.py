import json

with open("Question.json", 'r') as file:
    data = json.load(file)

sum=0
count=0
i=0
for records in data:
    if(data[i]["weight"] >5):
        sum += data[i]["weight"]
        count+=1
    i+=1

averageWeight = sum/count
print(averageWeight)