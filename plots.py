import time
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import sys
from sorting_assignment import bubblesort, quicksort

def plot_function_runtime(function):

    sizes = []
    times = []

    test_set = [100,200,300,400,500,600,700,800,900,1000]

    for i in range(10):
        for n in test_set:
            sizes.append(n)

            my_list = np.random.randint(low = 0, high = 100000, size = n)

            start_time = time.time()
            function(my_list)
            run_time = time.time() - start_time

            times.append(run_time)

    plt.figure(facecolor = 'white')
    plt.title(function.__name__)
    plt.scatter(sizes, times, marker = '.', alpha = 0.1)
    plt.ylabel('Run Time (s)')
    plt.xlabel('Random List Size')
    plt.show()

plot_function_runtime(quicksort)
plot_function_runtime(bubblesort)
