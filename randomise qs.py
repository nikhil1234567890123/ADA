import random
import time
import csv
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

if __name__ == "__main__":
    with open("rqs_analysis.csv", 'w', newline='') as file1:
        writer = csv.writer(file1)
        writer.writerow(['List Size', 'Time (seconds)'])
        
        input_sizes = list(range(1000, 100001, 1000))
        times = []
        
        for size in input_sizes:
            total_time = 0
            for _ in range(5):  # Repeat 5 times for better accuracy
                arr = random.sample(range(0, size * 2), size)
                start_time = time.time()
                randomized_quicksort(arr, 0, size - 1)
                end_time = time.time()
                execution_time = end_time - start_time
                total_time += execution_time
            average_time = total_time / 5  # Calculate average time
            times.append([size, average_time])
            writer.writerow([size, average_time])  # Write to CSV file
        
        sizes, runtimes = zip(*times)
        
        plt.plot(sizes, runtimes, label='Randomized QuickSort', marker='o')
        plt.xlabel('List Size (n)')
        plt.ylabel('Average Running Time (seconds)')
        plt.title('Randomized QuickSort Runtime Analysis')
        plt.legend()
        plt.grid(True)
        plt.show()
