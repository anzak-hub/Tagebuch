def add(*args):
    return sum(args)

def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def max_age(*args):
    return max(args)