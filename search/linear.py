# 선형 검색 : 무작위로 늘려놓은 데이터에서 검색을 수행
# O(N)
# 배열에서 key와 같은 요소를 찾아 인덱스를 반환하자
# 종료조건 1: key와 같은 요소를 찾았다.
# 종료조건 2: key와 같은 요소를 찾지 못하였다.
def seq_search(arr, key):
    i = 0
    while True:
        if i == len(arr):
            return -1
        if key == arr[i]:
            return i
        i += 1


# print(seq_search([1, 2, 4, 56, 7, 3, 4], 4))

# 보초법
# 두가지 종료 조건 중, 종료조건 2번(탐색이 끝날 때 까지 요소를 못찾는 다면)을 생략하는 방법
# 배열의 마지막에 찾고자 하는 값과 같은 값을 저장
#
def seq_search_sen(arr, key):
    last_idx = len(arr) - 1
    if arr[last_idx] == key:
        return last_idx
    i = 0
    while True:
        if key == arr[i]:
            return -1 if i == last_idx else i
        i += 1
