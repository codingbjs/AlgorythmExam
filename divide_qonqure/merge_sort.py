# 정렬된 베열 두개를 매개변수로 받아 하나의 정렬된 배열로 합쳐주는 함수
# [1,5,7,13] [2,4,9,12,15]
def merge(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    if i < len(arr1):
        res += arr1[i:len(arr1)]
    else:
        res += arr2[j:len(arr2)]

    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
