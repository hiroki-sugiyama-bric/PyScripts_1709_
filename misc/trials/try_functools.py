from functools import partial

def try_partial():
    def calc(a, b, c):
        return a + b * c

    print(calc(a=1, b=2, c=4))
    print(calc(a=1, b=3, c=4))

    calc_b_applied = partial(calc, b=3)

    print(calc_b_applied(a=1, c=4))





if __name__ == '__main__':
    try_partial()


