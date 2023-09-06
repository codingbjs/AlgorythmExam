def fibonacci_recur(n, memo=[None for _ in range(100)]):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    if memo[n] is not None:
        return memo[n]

    memo[n] = fibonacci_recur(n - 1, memo) + fibonacci_recur(n - 2, memo)
    return memo[n]


def fibo_dp_2(n):
    temp = [1, 1]

    if n < 2:
        return temp[-1]

    for i in range(2, n + 1):
        temp.append(temp[i - 2] + temp[i - 1])

    return temp

