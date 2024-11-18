from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
import matplotlib.pyplot as plt
import random


def gather_sort_data(sort_function, array_sizes):
    comparisons = []
    initializations = []

    for size in array_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        if sort_function.__name__ == "merge_sort":
            _, init_count, comp_count = sort_function(arr, 0, len(arr) - 1)
        elif sort_function.__name__ == "quick_sort":
            init_count, comp_count = sort_function(arr, 0, len(arr) - 1)
        else:
            init_count, comp_count = sort_function(arr)

        initializations.append(init_count)
        comparisons.append(comp_count)

    return comparisons, initializations


def compare_sort_algorithms(array_sizes, data_dict, title, ylabel):
    plt.figure(figsize=(12, 8))
    for sort_name, data in data_dict.items():
        plt.plot(array_sizes, data, marker='o', label=sort_name)
    plt.title(title)
    plt.xlabel("Array Size")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


array_sizes = [10, 50, 100, 200, 500]
comparisons_insertion, _ = gather_sort_data(insertion_sort, array_sizes)
comparisons_merge, _ = gather_sort_data(merge_sort, array_sizes)
comparisons_quick, _ = gather_sort_data(quick_sort, array_sizes)
comparisons_heap, _ = gather_sort_data(heap_sort, array_sizes)

data_comparisons = {
    "Insertion Sort": comparisons_insertion,
    "Merge Sort": comparisons_merge,
    "Quick Sort": comparisons_quick,
    "Heap Sort": comparisons_heap
}

compare_sort_algorithms(array_sizes, data_comparisons,
                        title="Comparison Counts", ylabel="Number of Comparisons")
