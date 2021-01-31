def multiples_3_5_n(n):
    i = 1
    total = 0
    while 3 * i < n or 5 * i < n:
        if 3 * i < n:
            total += 3 * i

        if 5 * i < n:
            if (5 * i) % 3 != 0:
                total += 5 * i
        i += 1
    return total


if __name__ == '__main__':
    print(multiples_3_5_n(1000))
