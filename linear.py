import random
import time
import matplotlib.pyplot as plt
import numpy as np


def ls(arr, key):
    comp = 0
    for i, element in enumerate(arr):
        comp += 1
        if element == key:
            return i, comp
    return -1, comp


def main():
    sizes = list(range(500, 5001, 500))  # Adjusted array sizes

    for num_trials in [10, 100, 1000, 10000]:
        print(f"Results for {num_trials} Trials:")
        print("Size\tAverage Time (µs)\tAverage Comparisons\tAverage Index")

        times = []
        comps = []
        indexes = []

        for size in sizes:
            arr = [random.randint(0, 2 * size - 1) for _ in range(size)] # generating an array with elements 0 to 2*size-1

            t_time = 0
            t_comp = 0
            t_indexes = 0

            for _ in range(num_trials):
                key = random.randint(0, 4 * size - 1)

                st_time = time.time()
                index, num_comparisons = ls(arr, key)
                end_time = time.time()

                t_time += (end_time - st_time)
                t_comp += num_comparisons
                t_indexes += index

            avg_time = (t_time / num_trials) * 1e6
            avg_comp = t_comp / num_trials
            avg_indexes = t_indexes / num_trials

            times.append(avg_time)
            comps.append(avg_comp)
            indexes.append(avg_indexes)

            print("{:7}\t{:16.2f}\t{:18.2f}\t{:13.2f}".format(size, avg_time, avg_comp, avg_indexes))

        # plotting the results for different sizes of arrays and for different num_trials
        plt.plot(sizes, times, marker='o', label=f'{num_trials} Trials')
        # adding a dotted trend line for reference 
        diagonal_line = np.linspace(min(times), max(times), len(sizes))
        plt.plot(sizes, diagonal_line, '--', color='gray', label='ideal linear search graph')
        plt.xlabel('Size of Array')
        plt.ylabel('Time (in micro sec)')
        plt.title(f'Linear Search Time Complexity (Number of Trials: {num_trials})')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    main()
