# 기존 방식 2n 개의 배열이 메모리에 올라간다.
# 이 방식은 n개의 배열만 메모리에 올라간다.
def merge_2(arr, low, mid, high):
    res = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1

    if i <= mid:
        res += arr[i:mid + 1]
    else:
        res += arr[j:high + 1]

    for i in range(low, high + 1):
        arr[i] = res[i - low]


def merge_sort_2(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort_2(arr, low, mid)
        merge_sort_2(arr, mid + 1, high)
        merge_2(arr, low, mid, high)
