class Grid:
    def __init__(self, lines: list[str]):
        self.lines = []
        for line in lines:
            self.lines.append(list(line.strip()))
        self.width = len(self.lines[0])
        self.height = len(self.lines)

    def __repr__(self):
        to_string = f"Grid(width={self.width}, height={self.height})\n"
        for line in self.lines:
            to_string += f"{''.join(line)}\n"
        return to_string

    def within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def print(self):
        for line in self.lines:
            print("".join(line))

    def get_char_at(self, x: int, y: int) -> str | None:
        if not self.within_bounds(x, y):
            return None

        return self.lines[y][x]


class GridPosition:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"GridPosition(x={self.x}, y={self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
