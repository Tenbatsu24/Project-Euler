import math


def find_divisors(n):
    divisors = []
    for i in range(1, round(math.sqrt(n)) + 1):
        if (n % i) == 0:
            divisors.append(i)
    for j in divisors[::-1]:
        divisors.append(n // j)
    return list(set(divisors))


def calculate_set_2n_sq_less_eq_n(n):
    set_of_divisors = set()
    divisors_of_n = find_divisors(n)
    count = len(divisors_of_n)
    if count == 1:
        print(f"n: {n} -> {n}")
        return {1}
    elif count == 2:
        if n == 2:
            print(f"n: {n} -> {1, n}")
            return {1, 2}
        else:
            print(f"n: {n} -> {1, 2, n}")
            return {1, 2, n}
    else:
        for i in divisors_of_n:
            for j in divisors_of_n[:count]:
                divisor = i * j
                if divisor <= n:
                    set_of_divisors.add(divisor)
                    if 2 * divisor <= n:
                        set_of_divisors.add(2 * divisor)
            count -= 1
        print(f"n: {n} -> {set_of_divisors}")
        return set_of_divisors


def calc_f(n):
    return sum([len(calculate_set_2n_sq_less_eq_n(i)) for i in range(1, n + 1)])


if __name__ == '__main__':
    print(calc_f(1000))
