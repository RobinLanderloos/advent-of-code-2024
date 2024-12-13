from GridModule.grid import *


class TrailHead:
    def __init__(self, x: int, y: int, score: int):
        self.x = x
        self.y = y
        self.score = score


def main():
    file = open("input.txt")
    lines = file.readlines()
    file.close()

    grid = Grid(lines)

    total_points = 0

    for grid_y in range(len(grid.lines)):
        for grid_x in range(len(grid.lines[grid_y])):
            if grid.get_char_at(grid_x, grid_y) == "0":
                trailhead_score = explore_trailhead(grid_x, grid_y, grid)
                print(f"{grid_x}, {grid_y} has score {trailhead_score}")
                total_points += trailhead_score
                # Check trailhead score

    print(f"Total points: {total_points}")


def explore_trailhead(x: int, y: int, grid: Grid) -> int:
    value = int(grid.get_char_at(x, y))
    next_value = value + 1
    points = 0
    points += scan_positions(x, y, next_value, grid)

    return points


def scan_positions(start_x: int, start_y: int, search_value: int, grid: Grid) -> int:
    left = start_x - 1
    right = start_x + 1
    top = start_y - 1
    bottom = start_y + 1
    next_value = search_value + 1
    search_value = str(search_value)

    points = 0

    if grid.get_char_at(start_x, start_y) == "9" and search_value == "10":
        print(f"Found 9 at {start_x}, {start_y}")
        points += 1


    # Check every direction for the value
    # If the value is found, search that location for the next value, until we reach a 9
    if grid.get_char_at(left, start_y) == search_value:
        points += scan_positions(left, start_y, next_value, grid)
    if grid.get_char_at(right, start_y) == search_value:
        points += scan_positions(right, start_y, next_value, grid)
    if grid.get_char_at(start_x, top) == search_value:
        points += scan_positions(start_x, top, next_value, grid)
    if grid.get_char_at(start_x, bottom) == search_value:
        points += scan_positions(start_x, bottom, next_value, grid)

    return points


if __name__ == "__main__":
    main()
