import sys


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    @classmethod
    def from_str(klass, start: str, end: str):
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        return Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))

    def points(self) -> set[Point]:
        # return points in between start - end(inclusive)
        lst = set()
        print(self.start, self.end)
        m0 = self.end.y - self.start.y
        m1 = self.end.x - self.start.x
        min_x, min_y = self.min()
        max_x, max_y = self.max()
        for x in range(min_x, max_x + 1):
            if ((x - self.start.x) * m0) % m1 == 0:
                y = ((x - self.start.x) * m0 // m1) + self.start.y
                if y >= min_y and y <= max_y:
                    lst.add(Point(x, y))
        return lst

    def min(self) -> tuple[int, int]:
        # return (min of x, min of y)
        return (self.start.x if self.start.x < self.end.x else self.end.x,
                self.start.y if self.start.y < self.end.y else self.end.y)

    def max(self) -> tuple[int, int]:
        # return (max of x, max of y)
        return (self.start.x if self.start.x > self.end.x else self.end.x,
                self.start.y if self.start.y > self.end.y else self.end.y)


class Grid:
    def __init__(self, lines: list[Line]):
        self.lines = lines
        x_min, y_min, x_max, y_max = 0, 0, 0, 0
        for line in lines:
            min_x, min_y = line.min()
            max_x, max_y = line.max()
            if min_x < x_min:
                x_min = min_x
            if min_y < y_min:
                y_min = min_y
            if max_x > x_max:
                x_max = max_x
            if max_y > y_max:
                y_max = max_y
        self.grids = [[0 for x in range(x_min, x_max + 1)]
                      for y in range(y_min, y_max + 1)]

    def __str__(self):
        return '\n'.join([
            ''.join(['.'.rjust(3) if cell == 0 else str(cell).rjust(3)
                     for cell in row])
            for row in self.grids]
        )

    def intersection(self):
        for line in self.lines:
            for point in line.points():
                self.grids[point.y][point.x] += 1


def parse_line(line) -> Line:
    start, end = line.split('->')
    return Line.from_str(start, end)


def prob1(filename):
    with open(filename) as f:
        lines = [parse_line(line) for line in f]
        grid = Grid(lines)
        grid.intersection()
        print(grid)


if __name__ == '__main__':
    assert len(sys.argv) >= 2
    prob1(sys.argv[1])
