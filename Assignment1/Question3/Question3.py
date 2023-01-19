from matplotlib import pyplot as plt
import string

alphabets = dict.fromkeys(string.ascii_lowercase,0)

with open("fintxt.txt", 'r', encoding='utf-8') as file:
    data = file.read()
data = data.lower()

totalFrequency = 0
for letter in alphabets:
    totalFrequency += data.count(letter)
    alphabets[letter] = data.count(letter)

letters = [k for k,v in alphabets.items()]
frequency = [(v/totalFrequency) for k,v in alphabets.items()]

for letter in alphabets:
    print(f"Letter: {letter} \t Frequency: {((alphabets[letter])/totalFrequency)}")

plt.bar(letters, frequency)
plt.xlabel("Letters")
plt.ylabel("Frequency")
plt.title("Frequency of Each Letter in The Count of Monte Cristo")
plt.savefig("barchart.png")
plt.show()

