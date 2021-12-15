import sys

if __name__ == '__main__':
    result = 0
    with open(sys.argv[1]) as f:
        for line in f:
            patterns, output = line.split(' | ')
            digits = output.strip().split(' ')
            result += sum([1 for digit in digits if len(digit)
                           in [2, 3, 4, 7]])
    print(result)
