def merge(arr, start, end):
    initializations_count = 0
    comparisons_count = 0
    mid = (start + end) // 2
    left = arr[start: mid + 1]
    right = arr[mid+1: end + 1]
    initializations_count += 2
    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        comparisons_count += 1
        if left[i] >= right[j]:
            arr[k] = right[j]
            initializations_count += 1
            j += 1
            k += 1
        else:
            arr[k] = left[i]
            initializations_count += 1
            i += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        initializations_count += 1
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        initializations_count += 1
        k += 1
        j += 1
    return initializations_count, comparisons_count


def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        mid = (start + end) // 2
        left_sorted, left_initializations, left_comparisons = merge_sort(
            arr, start, mid)
        right_sorted, right_initializations, right_comparisons = merge_sort(
            arr, mid + 1, end)
        merge_initializations, merge_comparisons = merge(arr, start, end)

        total_initializations = left_initializations + \
            right_initializations + merge_initializations
        total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    else:
        return arr, 0, 0

    return arr, total_initializations, total_comparisons
