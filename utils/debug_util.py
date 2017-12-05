def print_attrs(obj):
    for k in dir(obj):
        print(k)
        print(getattr(obj, k))
        print('')



if __name__ == '__main__':
    print_attrs('spam')
