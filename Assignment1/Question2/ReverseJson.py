import json

with open("Question2.json", "r") as reverse:
    dict = json.load(reverse)
reversedJson = dict[::-1]
with open("ReversedJson.json", "w") as reversed:
    json.dump(reversedJson, reversed)
