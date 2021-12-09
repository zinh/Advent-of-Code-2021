import sys


def tick(fishes):
    new_fishes = [0 for i in range(0, 9)]
    for remaining_time, count in enumerate(fishes):
        new_time = remaining_time - 1
        if new_time < 0:
            new_fishes[8] = count
            new_fishes[6] = count
        else:
            new_fishes[new_time] = new_fishes[new_time] + count
    return new_fishes


def prob1(filename):
    with open(filename) as f:
        line = f.readline()
        fishes_input = [int(number) for number in line.split(',')]
        fishes = [0 for i in range(0, 9)]
        for fish in fishes_input:
            fishes[fish] += 1
        print(fishes)
        for i in range(0, 256):
            fishes = tick(fishes)
        return sum(fishes)


if __name__ == '__main__':
    print(prob1(sys.argv[1]))
