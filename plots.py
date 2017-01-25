import time
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import sys
from sorting_assignment import bubblesort, quicksort

def n(x):
    out = []
    for i in x:
        out.append(i)
    return(out, r'$n$')

def n_squared(x):
    out = []
    for i in x:
        out.append(i**2)
    return(out, r'$n^2$')

def n_log_n(x):
    out = []
    for i in x:
        out.append(i*np.log(i))
    return(out, r'$nlog(n)$')

def plot_function_runtime(function, xscale):

    sizes = []
    times = []

    test_set = [100,200,300,400,500,600,700,800,900,1000]

    for i in range(100):
        for n in test_set:
            sizes.append(n)

            my_list = np.random.randint(low = 0, high = 100000, size = n)

            start_time = time.time()
            function(my_list)
            run_time = time.time() - start_time

            times.append(run_time)

    plt.figure(facecolor = 'white')
    plt.title('Sorting runtime of ' + function.__name__ + ' algorithm on random list of n integers \n(100 simulations at each n)')
    plt.scatter(xscale(sizes)[0], times, marker = '.', color = 'blue', alpha = 0.1)
    plt.ylabel('Run Time (s)')
    plt.xlabel(xscale(sizes)[1])
    plt.show()

plot_function_runtime(quicksort, n)
plot_function_runtime(bubblesort, n)
#plot_function_runtime(quicksort, n_log_n)
#plot_function_runtime(bubblesort, n_squared)
