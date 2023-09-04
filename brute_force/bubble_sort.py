def bubble_sort(arr):
    while True:
        swap = False
        i = 0
        while i < len(arr) - 1:
            print(arr)
            if arr[i] > arr[i + 1]:
                swap = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # temp = arr[i + 1]
                # arr[i + 1] = arr[i]
                # arr[i] = temp
            i += 1

        if not swap:
            return arr


def liner_sort(arr):
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j += 1
        i += 1

    return arr


print(bubble_sort([5, 1, 4, 2, 8]))
