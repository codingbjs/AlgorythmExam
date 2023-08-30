# 피보나치 수열
def fibonacci(n):
    if n < 1:
        return 0
    fib_sequence = [0, 1]
    for i in range(2, n):
        print(fib_sequence)
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence


def fibonacci_1(n):
    if n < 1:
        return 0
    prev, cur = 1, 1
    for i in range(3, n + 1):
        prev, cur = cur, prev + cur
    return cur


# 피보나치 재귀호출 - 재귀호출의 안좋은 예
def fibonacci_recur(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


# 피보나치 꼬리재귀 - 재귀호출 보다는 효율적
def fibonacci_tail(n, before=0, after=1):
    if n == 0:
        return 0
    elif n == 1:
        return after
    else:
        return fibonacci_tail(n - 1, after, before + after)
