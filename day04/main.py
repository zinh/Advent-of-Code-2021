import sys


class Cell:
    def __init__(self, number):
        self.value = int(number)
        self.is_called = False

    def called(self):
        self.is_called = True

    def __str__(self):
        if self.is_called:
            s = '[' + str(self.value) + ']'
        else:
            s = str(self.value)
        return s.rjust(5)


class Board:
    def __init__(self):
        self.data = []

    def __str__(self):
        return "\n".join(" ".join([str(cell) for cell in row])
                         for row in self.data)

    def append_row(self, row):
        self.data.append([Cell(cell) for cell in row])

    def call(self, number):
        for row in self.data:
            for cell in row:
                if cell.value == number:
                    cell.called()

    def is_win(self):
        # check rows
        for row in self.data:
            if all([cell.is_called for cell in row]):
                return True
        # check columns
        for column in zip(*self.data):
            if all([cell.is_called for cell in column]):
                return True
        return False

    def sum_unmark(self):
        return sum([cell.value for row in self.data for cell in row if not cell.is_called])


def parse_input(filename):
    boards = []
    with open(filename) as f:
        call_numbers = [int(s) for s in f.readline().split(',')]
        f.readline()
        board = Board()
        for line in f:
            numbers = line.split()
            if len(numbers) == 0:
                boards.append(board)
                board = Board()
            else:
                board.append_row(numbers)
        boards.append(board)
    return boards, call_numbers


def problem1(filename):
    boards, call_numbers = parse_input(filename)
    for number in call_numbers:
        for board in boards:
            board.call(number)
            if board.is_win():
                return board.sum_unmark() * number


def problem2(filename):
    boards, call_numbers = parse_input(filename)
    for number in call_numbers:
        deleted_boards = []
        for idx, board in enumerate(boards):
            board.call(number)
            if board.is_win():
                if len(boards) == 1:
                    return board.sum_unmark() * number
                else:
                    deleted_boards.append(idx)
        for idx in reversed(deleted_boards):
            del boards[idx]


if __name__ == '__main__':
    assert len(sys.argv) >= 2
    # print(problem1(sys.argv[1]))
    print(problem2(sys.argv[1]))
