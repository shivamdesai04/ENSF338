import json
from matplotlib import pyplot as plt

with open("golddata.json", 'r') as file:
    data = json.load(file)

print(data[0]["Date"][6:10])
print(data[0]["United States(USD)"])

usPrices = []
saPrices = []
Dates = []
i=0
for records in data:
    if(data[i]["Date"][6:10] == "2010"):
        usPrices.append(data[i]["United States(USD)"])
        Dates.append(data[i]["Date"])
        saPrices.append(data[i]["South Africa(ZAR)"])
    i+=1


# print(Dates)

plt.bar(Dates, usPrices)
plt.title("Gold prices for the US in 2010")
plt.xlabel("Date")
plt.ylabel("Prices (USD)")


plt.bar(Dates, saPrices)
plt.title("Gold prices for South Africa in 2010")
plt.xlabel("Date")
plt.ylabel("Prices (ZAR)")
plt.show()

# print(len(usPrices))