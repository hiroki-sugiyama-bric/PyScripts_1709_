def try_generator():
    def gen():
        yield 1
        yield 2
        yield 3


if __name__ == '__main__':
    try_generator()
