import math


def f(n):
    divisors = set({1, n})
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


if __name__ == '__main__':
    print(f(4001))
    print(f(2689))
