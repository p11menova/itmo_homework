import functools


def product(*args):
    return functools.reduce((lambda a, b: a * b), [*args])

