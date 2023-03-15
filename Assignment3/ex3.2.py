
import matplotlib.pyplot as plt
from timeit import timeit
import json

# Load array from ex2data.json and ex2task.json
with open('ex2data.json', 'r') as f:
    array = json.load(f)
with open('ex2tasks.json', 'r') as f:
    tasks = json.load(f)
    tasks = [{'target': t, 'best_mid_point': 0, 'best_time': [0, 0], 'times_list': []} for t in tasks]
           
def binary_search(array, target, midpoint):
    left = 0
    right = len(array) - 1
    while left <= right:
        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
        midpoint = (left + right) // 2
    return -1


def binary_search_timing(arr, task, midpoints):
    best_time = -1
    best_midpoint = 0
    target = task['target']
    for midpoint in midpoints:
        time_taken = timeit(lambda: binary_search(
            arr, target, midpoint), number=100)
        task['times_list'].append(time_taken)
        if time_taken < best_time or best_time == -1:
            best_time = time_taken
            best_midpoint = midpoint
    task['best_mid_point'] = best_midpoint
    task['best_time'][0] = best_time
    task['best_time'][1] = timeit(lambda: binary_search(arr, target, (len(array)//2)), number=100)
    return (best_midpoint, best_time)




midpoints = [i*25000 + 25000 for i in range(0, 39)]
for i, task in enumerate(tasks):
    best_midpoint, best_time = binary_search_timing(array, task, midpoints)
    print(
        f"Task {i}: Best midpoint: {best_midpoint}, time: {best_time:.9f}")


normal_mid_time_list = [task['best_time'][1] for task in tasks]
best_mid_point_time_list = [task['best_time'][0] for task in tasks]
mid_point_list = [task['best_mid_point'] for task in tasks]
test = [task['target'] for task in tasks]

plt.scatter(test, mid_point_list)
plt.yticks([i*25000 + 25000 for i in range(0, 39)])
plt.xlabel('Task')
plt.ylabel('Best midpoint timing')
plt.title('Midpoints for Binary Search')
plt.legend()
plt.show()