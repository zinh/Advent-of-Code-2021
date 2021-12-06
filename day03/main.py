import sys


def prod1(filename):
    m = [[0, 0] for i in range(0, 12)]
    with open(filename) as f:
        for line in f:
            for idx, digit in enumerate(list(line.strip())):
                if digit == '0':
                    m[idx][0] += 1
                else:
                    m[idx][1] += 1
    gamma = int(
        ''.join(['0' if idx[0] > idx[1] else '1' for idx in m]), base=2)
    epsilon = int(
        ''.join(['0' if idx[0] < idx[1] else '1' for idx in m]), base=2)
    print(gamma * epsilon)


def read_file(filename):
    with open(filename) as f:
        return [int(line, base=2) for line in f]


def oxygen(numbers):
    # most common
    position = numbers[0].bit_length() - 1
    while len(numbers) > 1 and position >= 0:
        c = count_bit(numbers, position)
        bit = 0 if c[0] > c[1] else 1
        numbers = filter_numbers(numbers, bit, position)
        position -= 1
    return numbers


def co2(numbers):
    # least common
    position = numbers[0].bit_length() - 1
    while len(numbers) > 1 and position >= 0:
        c = count_bit(numbers, position)
        bit = 0 if c[0] <= c[1] else 1
        numbers = filter_numbers(numbers, bit, position)
        position -= 1
    return numbers


def prob2(filename):
    numbers = read_file(filename)
    o = oxygen(numbers)[0]
    c = co2(numbers)[0]
    print(o, c)
    print(o * c)


def filter_numbers(numbers, bit, position):
    # filter out number that doesn't have bit b in position n
    mask = 1 << position
    if bit == 0:
        return [number for number in numbers if number & mask == 0]
    else:
        return [number for number in numbers if number & mask != 0]


def count_bit(numbers, position):
    # return count of 0, 1 at a position
    counts = [0, 0]
    mask = 1 << position
    for number in numbers:
        if number & mask == 0:
            counts[0] += 1
        else:
            counts[1] += 1
    return counts


if __name__ == '__main__':
    prob2(sys.argv[1])
