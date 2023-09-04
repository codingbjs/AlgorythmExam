# 이진 검색 - 데이터가 이미 오름차순, 또는 내림차순으로 정렬되어 있다는 전제 하에 검색하는 방법
# 1. 중앙 인덱스를 기준으로 배열을 두 파트로 분리
# 2. 검색 대상 데이터가 중앙 인덱스의 요소값 보다 크다면 우측, 작다면 좌측의 중앙 인덱스 값과 비교
# 3. 중앙 인덱스의 요소값과 검색 대상 데이터의 크기가 같으면 결과를 반환

def bin_search(arr, key):
    pl = 0
    pr = len(arr) - 1

    while pl <= pr:
        center = (pl + pr) // 2

        if arr[center] == key:
            return center
        elif key > arr[center]:
            pl = center + 1
        else:
            pr = center - 1

    return -1


# print(bin_search([1, 2, 3, 4, 5, 13, 26, 36], 4))
