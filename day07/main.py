import sys


def cost1(numbers, pos):
    return sum([abs(number - pos) for number in numbers])


def cost2(numbers, pos):
    return sum([abs(number - pos) * (abs(number - pos) + 1) // 2 for number in numbers])


def prob1(numbers):
    top = max(numbers)
    bottom = min(numbers)
    return min([cost1(numbers, pos) for pos in range(bottom, top + 1)])


def prob2(numbers):
    top = max(numbers)
    bottom = min(numbers)
    return min([cost2(numbers, pos) for pos in range(bottom, top + 1)])


if __name__ == '__main__':
    assert(len(sys.argv) > 1)
    with open(sys.argv[1]) as f:
        line = f.readline()
        numbers = [int(s) for s in line.split(',')]
        print(prob2(numbers))
