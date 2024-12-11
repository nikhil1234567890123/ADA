import time
import random
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    
    merged_arr = merge(L, R)
    return merged_arr

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

def analyze_merge_sort_time(arr_size):
    arr = [random.randint(0, 1000) for _ in range(arr_size)]
    
    start_time = time.time()
    _ = merge_sort(arr)
    end_time = time.time()
    
    return end_time - start_time

arr_sizes = [100, 500, 1000, 2000, 5000]  # Change this list as needed
times = []

for arr_size in arr_sizes:
    time_taken = analyze_merge_sort_time(arr_size)
    times.append(time_taken)

plt.plot(arr_sizes, times, marker='o')
plt.title('Merge Sort Time Complexity')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
