def unzip_and_flatten(zipped_seqs):
    """zipされたシーケンス群を、unzipした後にネストを解消して返却する。

    :param zipped_seqs:
    :return:
    """
    flatten = lambda seqs: [elm for seq in seqs for elm in seq]

    return tuple(flatten(e) for e in zip(*zipped_seqs))

