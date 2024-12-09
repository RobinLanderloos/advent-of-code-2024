class Grid:
    def __init__(self, lines: list[list[chr]]):
        self.lines = lines
        self.width = len(lines[0])
        self.height = len(lines)

    def within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def print(self):
        for line in self.lines:
            print("".join(line))


class GridPosition:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Antenna(x={self.x}, y={self.y})"


def main():
    print("Day 8 - Resonant Collinearity - Part 1")

    file_object = open("input.txt", "r")

    lines = file_object.readlines()
    file_object.close()

    grid = to_grid(lines)
    print("Input grid:")
    grid.print()

    # {'#': [Antenna(x=3, y=1), Antenna(x=6, y=7)], 'a': [Antenna(x=4, y=3), Antenna(x=5, y=5)]}

    antennas = get_antenna_dict(grid)

    antinodes = set[GridPosition]()

    for antenna in antennas:
        add_antinodes_for_frequency(antennas[antenna], grid, antinodes)

    print("Grid with antinodes:")
    grid.print()

    print(f"Number of antinodes: {len(antinodes)}")


def add_antinodes_for_frequency(antennas: list[GridPosition], grid: Grid, unique_antinode_positions: set[GridPosition]):
    for index in range(len(antennas)):
        antenna = antennas[index]

        for other_index in range(len(antennas)):
            if other_index == index:
                continue

            x_diff = abs(antenna.x - antennas[other_index].x)
            y_diff = abs(antenna.y - antennas[other_index].y)
            antinode_x = 0
            antinode_y = 0
            if antenna.x < antennas[other_index].x:
                antinode_x = antenna.x - x_diff
            elif antenna.x > antennas[other_index].x:
                antinode_x = antenna.x + x_diff
            if antenna.y < antennas[other_index].y:
                antinode_y = antenna.y - y_diff
            elif antenna.y > antennas[other_index].y:
                antinode_y = antenna.y + y_diff

            if grid.within_bounds(antinode_x, antinode_y) \
                    and grid.lines[antinode_y][antinode_x] != "#":
                unique_antinode_positions.add(GridPosition(antinode_x, antinode_y))
                grid.lines[antinode_y][antinode_x] = "#"


def get_antenna_dict(grid: Grid) -> dict[str, list[GridPosition]]:
    antennas = dict[str, list[GridPosition]]()
    for y in range(grid.height):
        for x in range(grid.width):
            current_letter = str(grid.lines[y][x])
            if current_letter == ".":
                continue
            if current_letter in antennas:
                antennas[current_letter].append(GridPosition(x, y))
            else:
                antennas[current_letter] = [GridPosition(x, y)]
    return antennas


def to_grid(lines: list[str]) -> Grid:
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return Grid(grid)


if __name__ == "__main__":
    main()
