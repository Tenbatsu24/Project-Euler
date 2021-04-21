def f(target_sum, choices):
    if target_sum < 0:
        return False
    elif target_sum == 0:
        return True

    for choice in choices:
        remainder = target_sum - choice
        new_choices = choices.copy()
        new_choices.remove(choice)
        if f(remainder, new_choices):
            return True

    return False


if __name__ == '__main__':
    print(f(7, [2, 4]))
    print(f(7, [2, 5]))
    print(f(500, [144, 336, 30, 66, 1338, 162, 318, 54, 84, 288, 126, 456]))
