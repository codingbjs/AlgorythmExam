def bubble_sort(arr):
    i = 0
    while i < len(arr) - 1:
        j = 0
        while j < len(arr) - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
    return arr


def bubble_sort1(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort2(arr):
    for i in range(len(arr) - 1, 0, -1):  # 4,3,2,1 감소 마지막 배열의 비교를 감소
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort3(arr):
    for i in range(len(arr) - 1, 0, -1):  # 4,3,2,1 감소 마지막 배열의 비교를 감소
        flg = False
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flg = True
        if not flg:
            return arr
    return arr



