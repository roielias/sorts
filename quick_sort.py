import random


def exchange(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return 2


def partition(a, p, r):
    sum_comparisons_count = 0
    sum_initializations_count = 0
    i = p - 1
    for j in range(p, r):
        if a[j] < a[r]:
            sum_comparisons_count += 1
            i += 1
            a[i], a[j] = a[j], a[i]
            sum_initializations_count += 2
    a[i], a[j] = a[j], a[i]
    sum_initializations_count += 2
    return i + 1, sum_initializations_count, sum_comparisons_count


def randomized_partition(a, p, r):
    i = random.randint(p, r)
    a[i], a[r] = a[r], a[i]
    pivot, init_count, comp_count = partition(a, p, r)
    return pivot, init_count + 2, comp_count


def quick_sort(a, p, r):
    total_initializations = 0
    total_comparisons = 0
    if p < r:
        q, init_count, comp_count = randomized_partition(a, p, r)
        total_initializations += init_count
        total_comparisons += comp_count
        left_init, left_comps = quick_sort(a, p, q - 1)
        right_init, right_comps = quick_sort(a, q + 1, r)

        total_initializations += left_init + right_init
        total_comparisons += left_comps + right_comps

    return total_initializations, total_comparisons
