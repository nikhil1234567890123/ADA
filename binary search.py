import numpy as np
import matplotlib.pyplot as plt
import math

# Binary search function
def bsearch(array, key):
    steps = 0
    high = len(array) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if array[mid] < key:
            low = mid + 1
        elif array[mid] > key:
            high = mid - 1
        else:
            break
    return steps

# Generate a sorted list with a random key
def gen(size):
    result = []
    temp = []
    actual_size = size
    for i in range(actual_size):
        temp.append(i)  # Generating a sorted list
    temp.sort()
    result.append(np.random.randint(0, actual_size))  # Random key
    result.append(temp)
    return result

# Calculate average steps for binary search
def calc(size):
    result = {"cum": 0, "avg": 0, "size": 0}
    for _ in range(100):
        list_for_key_and_arr = gen(size)
        steps = bsearch(list_for_key_and_arr[1], list_for_key_and_arr[0])
        result["size"] = size
        result["cum"] += steps
    result["avg"] = result["cum"] // 100
    return result

# Generate x values (sizes) and corresponding y values (average steps for binary search)
x_values = []
y_values = []
size = 10
while size <= 1000000:
    x_values.append(size)
    temp = calc(size)
    y_values.append(temp["avg"])
    size *= 10

# Generate x values for the benchmark (log2(n))
x_benchmark = np.array(x_values)
y_benchmark = np.log2(x_benchmark)

# Plotting
plt.plot(x_values, y_values, marker='o', label="Binary Search Performance")
plt.plot(x_benchmark, y_benchmark, label="Benchmark: log2(n)")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Size of Array (log scale)')
plt.ylabel('Average Steps (log scale)')
plt.title('Binary Search Performance vs Benchmark')
plt.grid(True)
plt.legend()
plt.show()