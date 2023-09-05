def partition_2(arr, low, high):
    pivot_item = arr[low]
    i = low + 1
    j = high
    while i <= j:
        while arr[i] < pivot_item and i < j:
            i += 1

        while arr[j] > pivot_item and j > i:
            j -= 1

        if i <= j:  # i와 j의 값이 같거나 역전되지 않았을 때만 교환
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    pivot_point = j
    arr[low], arr[pivot_point] = arr[pivot_point], arr[low]
    return pivot_point


def quick_sort_2(arr, low, high):
    if low < high:
        pivot_point = partition_2(arr, low, high)
        quick_sort_2(arr, low, pivot_point - 1)
        quick_sort_2(arr, pivot_point + 1, high)
