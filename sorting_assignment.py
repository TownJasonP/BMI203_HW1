import time
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import sys

def bubblesort(some_list):
    if len(some_list) == 0:
        return([])
    iteration = 1
    while iteration < len(some_list):
        for i in range(len(some_list)-iteration):
            if some_list[i] > some_list[i + 1]:
                temp = some_list[i]
                some_list[i] = some_list[i + 1]
                some_list[i + 1] = temp
        iteration += 1
    return(some_list)


def quicksort(some_list):

    if len(some_list) == 0:
        return([])

    lesser = []
    equal = []
    greater = []

    if len(some_list) > 1:
        pivot = some_list[int(len(some_list)/2)]
        for i in some_list:
            if i < pivot:
                lesser.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                greater.append(i)
        return(quicksort(lesser)+equal+quicksort(greater))
    else:
        return(some_list)

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
