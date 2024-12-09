class Grid:
    def __init__(self, lines: list[list[chr]]):
        self.lines = lines
        self.width = len(lines[0])
        self.height = len(lines)

    def within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    @classmethod
    def from_lines(cls, lines: list[str]):
        grid = []
        for line in lines:
            grid.append(list(line.strip()))
        return Grid(grid)

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

    grid = Grid.from_lines(lines)
    print("Input grid:")
    grid.print()

    antennas = get_antenna_dict(grid)

    antinodes = set[GridPosition]()

    for antenna in antennas:
        add_antinodes_for_frequency(antennas[antenna], grid, antinodes)

    print("Grid with antinodes:")
    grid.print()

    print(f"Number of antinodes: {len(antinodes)}")


def add_antinodes_for_frequency(antennas: list[GridPosition], grid: Grid, unique_antinode_positions: set[GridPosition]):
    """
    Takes a list of antennas and checks their resonance on the given grid, it then returns all unique positions for antinodes
    """

    for index in range(len(antennas)):
        antenna = antennas[index]

        for other_index in range(len(antennas)):
            if other_index == index:
                continue

            x_diff = abs(antenna.x - antennas[other_index].x)
            y_diff = abs(antenna.y - antennas[other_index].y)
            antinode_x = 0
            antinode_y = 0
            modifier = 0
            while grid.within_bounds(antinode_x, antinode_y):
                if antenna.x < antennas[other_index].x:
                    antinode_x = antenna.x - (x_diff * modifier)
                elif antenna.x > antennas[other_index].x:
                    antinode_x = antenna.x + (x_diff * modifier)
                if antenna.y < antennas[other_index].y:
                    antinode_y = antenna.y - (y_diff * modifier)
                elif antenna.y > antennas[other_index].y:
                    antinode_y = antenna.y + (y_diff * modifier)

                if grid.within_bounds(antinode_x, antinode_y) \
                        and grid.lines[antinode_y][antinode_x] != "#":
                    unique_antinode_positions.add(GridPosition(antinode_x, antinode_y))
                    grid.lines[antinode_y][antinode_x] = "#"
                modifier += 1



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




if __name__ == "__main__":
    main()
