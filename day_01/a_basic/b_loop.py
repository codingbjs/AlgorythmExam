# 1+2+3+...n = sum
# 매개변수로 n을 입력받아 위와 같은 형태로 출력

def q1(n):
    _sum = 0
    num_str = ""
    for num in range(1, n + 1):
        num_str += f"{num}"
        if num < n:
            num_str += " + "
        _sum += num
    print(f" {num_str} = {_sum}")


# 다이아몬드 별찍기
# 사용자로 부터 3이상의 자연수를 입력 받아
# 한 변의 길이가 사용자의 입력값인 다이아몬드를 그리시오
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

def print_diamond(cnt):
    if cnt < 3:
        print("한 변의 길이는 3 이상이어야 합니다.")
        return

    # 위쪽 삼각형 출력
    for i in range(1, cnt + 1, 2):
        spaces = (cnt - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)

    # 아래쪽 삼각형 출력
    for i in range(cnt - 2, 0, -2):
        spaces = (cnt - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)


if __name__ == '__main__':
    q1(10)
    print_diamond(6)

