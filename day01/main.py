def prod1():
    last_number = 100000
    freq = 0

    with open('input') as f:
        for line in f:
            n = int(line)
            if n > last_number:
                freq = freq + 1
            last_number = n
    print(freq)


def prod2():
    with open('input') as f:
        lines = [int(i) for i in f]
        lst = [sum(triplet)
               for triplet in zip(lines[0:-2], lines[1:-1], lines[2:])]

        last_number = 100000
        freq = 0

        for n in lst:
            if n > last_number:
                freq += 1
            last_number = n
        print(freq)


if __name__ == '__main__':
    prod2()
