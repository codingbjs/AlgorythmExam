"""
 n 개의 정수로 이루어진 수열
이중 연속된 몇개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구한다.
단, 수는 한개 이상 선택해야 한다.
"""


def sub_sum(arr):
    sum_list = [arr[0]]
    for i in range(1, len(arr)):
        res = sum_list[i - 1] + arr[i]

        # if res > arr[i]:
        #     sum_list.append(res)
        # else:
        #     sum_list.append(arr[i])

        sum_list.append(max(res, arr[i]))

    return max(sum_list)


def sub_sum_1(arr):
    sum_arr = [arr[0]]

    for e in arr[1:]:
        sum_arr.append(max(sum_arr[-1] + e, e))

    return max(sum_arr)


print(sub_sum([10, -4, 3, 1, 5, 6, -35, 12, 21, -1]))
print(sub_sum_1([10, -4, 3, 1, 5, 6, -35, 12, 21, -1]))
