def try_unzip():
    a = ([1, 2], [3, 4])
    b = ([5], [6])

    flatten = lambda seqs: [elm for seq in seqs for elm in seq]

    for e in zip(*(a, b)):
    # for e in zip(*([], [])):
        print(e)
        # print(flatten(e))

    # print(tuple(flatten(e) for e in zip(*(a, b))))

    print(unzip_and_flatten((a, b)))

def unzip_and_flatten(zipped_seqs):
    flatten = lambda seqs: [elm for seq in seqs for elm in seq]

    return tuple(flatten(e) for e in zip(*zipped_seqs))


if __name__ == '__main__':
    # try_unzip()
    print(unzip_and_flatten(([], [])))
