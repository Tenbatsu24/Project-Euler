def fib_even_sum(n):
    a, b = 1, 2
    total = 0
    while b < n:
        if (b % 2) == 0:
            total += b
        a, b = b, a + b
    return total


if __name__ == '__main__':
    print(fib_even_sum(4000000))
