def even(n):
    return n * 3 + 1


def odd(n):
    return n / 2


def is_odd_even(n):
    if n % 2 != 0: return even(n)
    return odd(n)
