# 종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다.
# 제일 작은 종말의 수는 666이고, 그 다음으로 큰 수는 1666,2666,3666,... 이다
# 사용자로 부터 전달 받은 n 번째에 해당하는 종말의 수를 구하는 doom_day 함수를 구현 하시오
# 매개변수로 전달 받은 숫자 까지 존재하는 종말의 숫자(666 이 들어간 숫자)를 담은 배열을 리턴
def doom_day(n):
    doom_list = []
    i = 666
    while True:
        if len(doom_list) == n:
            return doom_list
        doom_list.append(i)
        i += 1000


def doom_day1(n):
    doom_list = []
    doom_num = 666
    i = 0
    while True:
        if i == doom_num:
            doom_list.append(i)
            doom_num += 1000
            if len(doom_list) == n:
                return doom_list
        i += 1


"""
# 아홉 난쟁이 중 백설공주와 일곱 난쟁이의 일곱 난쟁이를 찾으시오
# 일곱난쟁이의 키의 합는 100입니다.
# 전달 받은 배열의 요소 중 7요소의 부분합이 100이 되게끔 하는 로직을 작성하고
# 부분합이 100이되는 요소 7개를 배열로 반환하시오
"""


def dwarf(arr):
    for i in range(len(arr)):
        tot = 0
        tot_list = {}
        for j in range(len(arr)):
            if j == i or j == i + 1:    # 7개의 배열 요소만 더하기 위해 2개 의 요소는 제외
                continue
            tot += arr[j]
            tot_list[j] = arr[j]
        if tot == 100:
            return tot_list
