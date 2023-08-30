# 피보나치 수열
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        print(fib_sequence)
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence
