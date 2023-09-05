def partition(arr, low, high):
    pivot_item = arr[low]
    j = low
    for i in range(low + 1, high + 1):
        if arr[i] < pivot_item:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]

    pivot_point = j
    arr[low], arr[pivot_point] = arr[pivot_point], arr[low]

    return j


def quick_sort(arr, low, high):
    if low < high:
        pivot_point = partition(arr, low, high)
        quick_sort(arr, low, pivot_point - 1)
        quick_sort(arr, pivot_point + 1, high)
