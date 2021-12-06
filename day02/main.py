def prod1():
    h, d, aim = 0, 0, 0
    with open('input') as f:
        for line in f:
            cmd, s = line.split(' ')
            n = int(s)
            if cmd == 'forward':
                h += n
                d += aim * n
            elif cmd == 'down':
                aim += n
            elif cmd == 'up':
                aim -= n
        print(abs(h) * abs(d))


if __name__ == '__main__':
    prod1()
