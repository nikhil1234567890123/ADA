import random
import time
import csv
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10**6) # Recursion limit ko badhane ke liye

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

if __name__ == "__main__":
    with open("qs_5.csv", 'w', newline='') as file1:
        writer = csv.writer(file1)
        writer.writerow(['List Size', 'Time (seconds)'])
        L1 = list(range(1000, 100001, 1000))
        times_avg = []
        times_worst = []
        times_best = []
        for i in L1:
            # Average Case
            arr_avg = random.sample(range(0, i * 2), i)
            start_time = time.time()
            quicksort(arr_avg, 0, len(arr_avg) - 1)
            end_time = time.time()
            execution_time_avg = end_time - start_time
            times_avg.append(execution_time_avg)
            
            # Worst Case
            arr_worst = list(range(i, 0, -1))
            start_time = time.time()
            quicksort(arr_worst, 0, len(arr_worst) - 1)
            end_time = time.time()
            execution_time_worst = end_time - start_time
            times_worst.append(execution_time_worst)
            
            # Best Case
            arr_best = list(range(i))
            start_time = time.time()
            quicksort(arr_best, 0, len(arr_best) - 1)
            end_time = time.time()
            execution_time_best = end_time - start_time
            times_best.append(execution_time_best)
            
            writer.writerow([i, execution_time_avg, execution_time_worst, execution_time_best]) # Write to CSV file
        
        plt.plot(L1, times_avg, label='Average Case', marker='o')
        plt.plot(L1, times_worst, label='Worst Case', marker='o')
        plt.plot(L1, times_best, label='Best Case', marker='o')
        plt.xlabel('List Size')
        plt.ylabel('Time (seconds)')
        plt.title('Quick Sort Analysis')
        plt.legend()
        plt.grid(True)
        plt.show()
