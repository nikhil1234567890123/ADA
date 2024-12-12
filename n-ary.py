import random
import time
import csv
import matplotlib.pyplot as plt

def n_ary_search(graph_function, start, end, cuts):
    precision = 0.001
    while end - start > precision:
        interval_size = (end - start) / (cuts + 1)
        cut_points = [start + i * interval_size for i in range(1, cuts + 1)]
        times = [measure_time(graph_function, point) for point in cut_points]
        min_index = times.index(min(times))
        start = cut_points[min_index - 1]
        end = cut_points[min_index]
    return (start + end) / 2

def measure_time(graph_function, point):
    start_time = time.time()
    _ = graph_function(point)
    end_time = time.time()
    return end_time - start_time

def graph_function(x):
    return (x - 3) ** 2

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['no. of cuts', 'time_lapsed'])
        csvwriter.writerows(data)

def main():
    cuts = [3, 5, 10]
    num_iterations = 1000
    num_samples = 10000
    time_arr = []

    for i in cuts:
        time_lapsed_total = 0
        for _ in range(num_iterations):
            start = time.time()
            _ = n_ary_search(graph_function, 0, num_samples * 10, i)
            end = time.time()
            time_lapsed_total += (end - start)
        time_lapsed_avg = (time_lapsed_total / num_iterations) * 1000  # Convert to milliseconds
        time_arr.append([i, time_lapsed_avg])

    write_to_csv('data.csv', time_arr)
    plot_graph(time_arr)

def plot_graph(data):
    cuts, time_lapsed = zip(*data)
    plt.plot(cuts, time_lapsed, marker='o', linestyle='-')
    plt.xlabel('Number of divisions (cuts)')
    plt.ylabel('Time in milliseconds')
    plt.show()

if __name__ == "__main__":
    main()
