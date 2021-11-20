import timeit


def time_it_dec(func):

    def wrapper():
        print(timeit.timeit(func))

    wrapper()


