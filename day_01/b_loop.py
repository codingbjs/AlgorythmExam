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
    ln = ''
    for i in range(cnt):
        bl = ''
        st = ''
        for j in range(cnt - i):
            bl += ' '
        for k in range(2 * i + 1):
            st += '*'
        ln = bl + st
        print(ln)

    for i in range(cnt - 1, 0, -1):
        bl = ''
        st = ''
        for j in range(cnt + 1 - i):
            bl += ' '
        for k in range(2 * i - 1):
            st += '*'
        ln = bl + st
        print(ln)


def print_diamond_1(cnt):
    for i in range(cnt):
        print(' ' * (cnt - i) + '*' * (i * 2 + 1))
    for i in range(1, cnt):
        print(' ' * (i + 1) + '*' * ((cnt * 2 - 1) - (2 * i)))


if __name__ == '__main__':
    q1(10)
    print_diamond(3)
    print_diamond_1(3)
