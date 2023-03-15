#inefficient implementation of sort of an array
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#efficient implementation of sort of an array
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


from timeit import timeit
import matplotlib.pyplot as plt
import random
import numpy

if __name__ == "__main__":
    data = list(range(1, 2001))
    linear_search_times = []
    binary_search_times = []

    for i in range(100):
        target = random.randint(1, len(data)-1)
        linear_search_times.append(timeit(lambda: linear_search(data, target), number=1))
        binary_search_times.append(timeit(lambda: binary_search(data, target), number=1))

    # printing minimum and average times for each search 
    print("Linear Search")
    print(f"Minimum time: {min(linear_search_times):.9f} seconds")
    print(f"Average time: {numpy.mean(linear_search_times):.9f} seconds")
    print("")
    print("Binary Search")
    print(f"Minimum time: {min(binary_search_times):.9f} seconds")
    print(f"Average time: {numpy.mean(binary_search_times):.9f} seconds")

    #plotting a histogram showing search times
    plt.hist(linear_search_times, label='Linear Search')
    plt.hist(binary_search_times, label='Binary Search')
    plt.xlabel('Execution Time (s)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()