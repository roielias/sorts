def insertion_sort(arr):
    initializations_count = 0
    comparisons_count = 0
    for j in range(1, len(arr)):
        i = j - 1
        key = arr[j]
        while i >= 0 and key < arr[i]:
            comparisons_count += 1
            arr[i + 1] = arr[i]
            initializations_count += 1
            i -= 1
        comparisons_count += 1
        arr[i + 1] = key
        initializations_count += 1
    return (initializations_count, comparisons_count)
