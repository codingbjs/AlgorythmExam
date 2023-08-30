# 양수 팩토리얼
def factorial(a):
    if a <= 0:
        return 1
    fat = 1
    for i in range(1, a + 1):
        fat *= i
    return fat


# 양수 팩토리얼 재귀 호출
def factorial_redef(n):
    if n <= 0 or n == 1:
        return 1
    return n * factorial_redef(n - 1)

# 꼬리재귀
# 재귀호출 명령이 함수의 제일 마지막에 오면서, 함수의 리턴값이 수식의 일부이지 않는 방식
# 꼬리개재귀로 작성된 코드는 컴파일러가 내부적으로 반복문으로 변경하여 실행 -> 프레임이 열리고 닫히는 비용이 발생하지 않음
# 파이썬는 꼬리재귀 최적화를 지원하지 않는다.
