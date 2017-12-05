def try_open():
    path = '../data/images/pikachu.jpg'
    with open(path, mode='rb') as f:
        print(f)

if __name__ == '__main__':
    try_open()


