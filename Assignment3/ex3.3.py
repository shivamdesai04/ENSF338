import sys

list = []
previous_size = 0

for i in range(64):
    list.append(i)
    size = sys.getsizeof(list)
    if size != previous_size:
        print(f"Capacity changed at size {i}: {size} bytes")
        previous_size = size

print(list)