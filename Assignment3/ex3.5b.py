
import heapq
import matplotlib.pyplot as plt
import numpy 
from timeit import timeit
import random

class InefficientPriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
        self.queue.sort(reverse=True)

    def pop(self):
        if len(self.queue) == 0:
            return None
        max_index = 0
        max_value = self.queue[0]
        for i in range(1, len(self.queue)):
            if self.queue[i] > max_value:
                max_value = self.queue[i]
                max_index = i
        del self.queue[max_index]
        return max_value


class EfficientPriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        heapq.heappush(self.queue, item)

    def pop(self):
        return heapq.heappop(self.queue)


insert_time_inefficient_results = []
extract_time_inefficient_results = []
insert_time_efficient_results = []
extract_time_efficient_results = []

numbers = [random.randint(0, 1000) for i in range(0, 1000)]

pq1 = InefficientPriorityQueue()
pq2 = EfficientPriorityQueue()


for i in range(1000):
    insert_time_inefficient_results.append(
        timeit(lambda: [pq1.push(x) for x in numbers], number=1)
    )
    extract_time_inefficient_results.append(
        timeit(lambda: [pq1.pop() for x in numbers], number=1)
    )

    insert_time_efficient_results.append(
        timeit(lambda: [pq2.push(x) for x in numbers], number=1)
    )
    extract_time_efficient_results.append(
        timeit(lambda: [pq2.pop() for x in numbers], number=1)
    )


print("Average of measured values:")
print("Insertion timing:")
print(f"Efficient Priority Queue: {numpy.mean(insert_time_efficient_results):.9f}")
print(f"Inefficient Priority Queue: {numpy.mean(insert_time_inefficient_results):.9f}")
print("")
print("Extraction timing:")
print(f"Efficient Priority Queue: {numpy.mean(extract_time_efficient_results):.9f}")
print(f"Inefficient Priority Queue: {numpy.mean(extract_time_inefficient_results):.9f}")

#plotting graphs
plt.figure(1)
plt.hist([insert_time_efficient_results, insert_time_inefficient_results], label=["efficient", "inefficient"])
plt.title('Insertion timing')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.legend()

plt.figure(2)
plt.hist([extract_time_efficient_results, extract_time_inefficient_results], label=["efficient", "inefficient"])
plt.title('Extraction timing')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.legend()
plt.show()