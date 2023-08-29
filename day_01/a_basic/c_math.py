# 소수 판단 - 1과 자신의 수로만 나누어 지는 수
from math import sqrt


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
    for i in range(1, num):
        if num % i == 0:
            su.append(i)
    print(f"{num} 약수 : {su}")
