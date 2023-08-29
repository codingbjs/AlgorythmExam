from math import sqrt


# 소수 판단 - 1과 자신의 수로만 나누어 지는 수
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_2(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


# 2 부터 입력 받은 값 사이에 존재하는 소수를 구해 리스트로 반환하시오
def is_prime_list(num):
    prime_list = []
    for check_num in range(2, num):
        if is_prime_2(check_num):
            prime_list.append(check_num)
    return prime_list


def su_num(num):
    su = []
    for i in range(1, num + 1):
        if num % i == 0:
            su.append(i)
    return su


def gcd1(a, b):
    a_su = su_num(a)
    b_su = su_num(b)
    print(a_su)
    print(b_su)
    common_numbers = set(a_su) & set(b_su)
    if not common_numbers:
        return None  # 공통된 수가 없는 경우
    largest = max(common_numbers)
    return largest


def gcd2(a, b):
    _min = b
    if a < _min:
        _min = a

    for i in range(_min, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# 유클리드 호제법을 활용한 최대공약수 구하기
# a, b 두 수가 있을때 (a > b)
# a 를 b로 나눈 나머지는 두 수의 최대공약수의 배수다

def gcd3(a, b):
    if a < b:
        _min = a
        a = b
        b = _min

    while b > 0:
        # print(a, b)
        a, b = b, a % b
    return a


def lcm1(a, b):
    max_val = max(a, b)
    while True:
        if max_val % a == 0 and max_val % b == 0:
            return max_val
        max_val += 1


# 최소 공배수
def lcm2(a, b):
    return (a * b) / gcd3(a, b)
