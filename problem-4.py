def is_palindrome(n):
    return str(n) == str(n)[::-1]


def f():
    curr_max = -1
    for i in range(10, 100):
        for j in range(100, 1000):
            n = 11*i*j
            if len(str(11*i)) == 3 and len(str(j)) == 3 and n > curr_max and is_palindrome(n):
                curr_max = n
    return curr_max


if __name__ == '__main__':
    print(f())
