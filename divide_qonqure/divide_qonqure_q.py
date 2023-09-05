"""
거듭제곱 최적화
매개변수 A, B를 받아 A를 B번 곱한 값을 반환하는 함수를 작성하시오
해당 함수의 사간 복잡도는 O(logN)입니다.
B가 짝수 일때
A^B = A^(B//2) * A ^ (B//2)
B가 홀수 일때
A^B = A^(B//2) * A ^ (B//2) * A
"""


def power(a, b):
    if b == 0:
        return 1
    print(f"a = {a}, b = {b}")
    if b % 2 == 0:
        half_power = power(a, b // 2)
        return half_power * half_power
    else:
        half_power = power(a, b // 2)
        return half_power * half_power * a


print(power(2, 6))
