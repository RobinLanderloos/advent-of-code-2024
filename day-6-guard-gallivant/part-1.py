import enum


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def to_string(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    @classmethod
    def from_character(cls, character: chr):
        match character:
            case "^":
                cls.value = Direction.UP
            case "V":
                cls.value = Direction.DOWN
            case "<":
                cls.value = Direction.LEFT
            case ">":
                cls.value = Direction.RIGHT
        return cls.value


unique_visited = set[Position]()


def main():
    file_object = open("./input.txt", "r")

    lines = file_object.read().splitlines()

    print(f"Lines ({len(lines)}):")

    grid = list[list[chr]]()

    for line in lines:
        grid.append(list[chr](line))

    _, start_position = get_positions(lines)
    predict_path(grid, start_position)


def predict_path(grid: list[list[chr]], start_position: Position):
    reached_end = False
    position = start_position

    while not reached_end:
        position, reached_end = take_step(grid, position)

    print(f"Unique steps: {len(unique_visited)}")


def take_step(grid: list[list[chr]], position: Position) -> tuple[Position, bool]:
    direction = Direction.from_character(grid[position.x][position.y])
    print(f"Taking step {direction}")
    match direction:
        case Direction.UP:
            return move_up(position, grid)
        case Direction.RIGHT:
            return move_right(position, grid)
        case Direction.DOWN:
            return move_down(position, grid)
        case Direction.LEFT:
            return move_left(position, grid)

    return position, True


def move_left(position: Position, grid: list[list[chr]]) -> tuple[Position, bool]:
    print("Moving left")
    global unique_visited

    # Reached end of grid
    if position.y - 1 < 0:
        grid[position.x][position.y] = "X"
        unique_visited.add(position)
        return Position(position.x, position.y), True

    # Is next position an obstacle? Turn right
    is_obstacle = grid[position.x][position.y - 1] == "#"
    if is_obstacle:
        grid[position.x][position.y] = "^"
        return Position(position.x, position.y), False

    # Move left
    grid[position.x][position.y] = "X"
    unique_visited.add(position)
    grid[position.x][position.y - 1] = "<"
    return Position(position.x, position.y - 1), False


def move_down(position: Position, grid: list[list[chr]]) -> tuple[Position, bool]:
    print("Moving down")
    global unique_visited

    # Reached end of grid
    if position.x + 1 >= len(grid):
        grid[position.x][position.y] = "X"
        unique_visited.add(position)
        return Position(position.x, position.y), True

    # Is next position an obstacle? Turn left
    is_obstacle = grid[position.x + 1][position.y] == "#"
    if is_obstacle:
        grid[position.x][position.y] = "<"
        return Position(position.x, position.y), False

    # Move down
    grid[position.x][position.y] = "X"
    unique_visited.add(position)
    grid[position.x + 1][position.y] = "v"
    return Position(position.x + 1, position.y), False


def move_right(position: Position, grid: list[list[chr]]) -> tuple[Position, bool]:
    print("Moving right")
    global unique_visited

    # Reached end of grid
    if position.y + 1 >= len(grid[position.x]):
        grid[position.x][position.y] = "X"
        unique_visited.add(position)
        return Position(position.x, position.y), True

    # Is next position an obstacle? Turn left
    is_obstacle = grid[position.x][position.y + 1] == "#"
    if is_obstacle:
        grid[position.x][position.y] = "V"
        return Position(position.x, position.y), False

    # Move right
    grid[position.x][position.y] = "X"
    unique_visited.add(position)
    grid[position.x][position.y + 1] = ">"
    return Position(position.x, position.y + 1), False


def move_up(position: Position, grid: list[list[chr]]) -> tuple[Position, bool]:
    print("Moving up")
    global unique_visited

    # Reached end of grid
    if position.x - 1 < 0:
        grid[position.x][position.y] = "X"
        unique_visited.add(position)
        return Position(position.x, position.y), True

    # Is next position an obstacle? Turn right
    is_obstacle = grid[position.x - 1][position.y] == "#"
    if is_obstacle:
        grid[position.x][position.y] = ">"
        return Position(position.x, position.y), False

    # Move up
    grid[position.x][position.y] = "X"
    unique_visited.add(position)
    grid[position.x - 1][position.y] = "^"
    return Position(position.x - 1, position.y), False


def get_positions(lines: list[str]) -> tuple[dict[Position, Position], Position]:
    obstacle_positions = {}
    start_position = Position(0, 0)

    for line_index in range(len(lines)):
        line = lines[line_index]
        for character_index in range(len(line)):
            character = line[character_index]
            if character == "#":
                position = Position(line_index, character_index)
                obstacle_positions[position] = position
            elif character != ".":
                start_position = Position(line_index, character_index)

    print(f"Obstacle positions ({len(obstacle_positions)}):")
    print(obstacle_positions)

    print(f"Start position ({start_position.x}, {start_position.y})")

    return obstacle_positions, start_position


if __name__ == "__main__":
    main()
