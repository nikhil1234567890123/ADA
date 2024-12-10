import random
import timeit
import matplotlib.pyplot as plt

def minmax1(arr, n):
    max_val = arr[0]
    min_val = arr[0]
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
    final_list = [min_val, max_val]
    return final_list

def minmax2(arr, low, high):  # Converted minmax3 to minmax2
    arr_max = arr[low]
    arr_min = arr[low]
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:
        mid = (low + high) // 2
        arr_max1, arr_min1 = minmax2(arr, low, mid)  # Changed minmax3 to minmax2
        arr_max2, arr_min2 = minmax2(arr, mid + 1, high)  # Changed minmax3 to minmax2
        return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

n_list = list(range(1000, 40001, 2000))
time_list1 = []
time_list2 = []

for n in n_list:
    num_list = random.sample(range(1, 2 * n), n)
    
    start = timeit.default_timer()
    minmax1(num_list, len(num_list))
    end = timeit.default_timer()
    time_list1.append((end - start) / n)

    start = timeit.default_timer()
    minmax2(num_list, 0, len(num_list) - 1)  # Changed minmax3 to minmax2
    end = timeit.default_timer()
    time_list2.append((end - start) / n)

# Plotting
plt.plot(n_list, time_list1, label='minmax1')
plt.plot(n_list, time_list2, label='minmax2')  # Updated label to minmax2
plt.xlabel("List Size")
plt.ylabel("Time Taken (seconds per operation)")
plt.title("Minmax Algorithms Performance")
plt.legend()
plt.show()
