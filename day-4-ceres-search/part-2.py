XMAS = "MAS"
OUT_OF_BOUNDS_LENGTH = 2


def main():
    file_object = open("./input.txt", "r")

    lines = file_object.readlines()

    total = 0

    for line_index in range(len(lines)):
        line = lines[line_index]
        for character_index in range(len(line)):
            if line[character_index] == XMAS[1]:
                total += search_x_mas(lines, character_index, line_index)

    print(f"Total: {total}")


def print_lines(lines: [str], line_index: int, character_index: int):
    print("----------------------")
    for i in range(len(lines)):
        to_print = ""
        for j in range(len(lines[i])):
            if i == line_index and j == character_index:
                to_print += "X"
            else:
                to_print += lines[i][j]
        print(to_print)
    print("----------------------")


def search_x_mas(lines: [str], character_index: int, line_index: int) -> int:
    if (out_of_south_bounds(line_index, len(lines))
            or out_of_east_bounds(character_index, len(lines[0]))
            or out_of_west_bounds(character_index)
            or out_of_north_bounds(line_index)):
        return 0

    if lines[line_index - 1][character_index - 1] == XMAS[0] and lines[line_index + 1][character_index + 1] == XMAS[2]:
        found_north_west_south_east = True
    elif lines[line_index - 1][character_index - 1] == XMAS[2] and lines[line_index + 1][character_index + 1] == XMAS[
        0]:
        found_north_west_south_east = True
    else:
        return 0

    if lines[line_index - 1][character_index + 1] == XMAS[0] and lines[line_index + 1][character_index - 1] == XMAS[2]:
        found_north_east_south_west = True
    elif lines[line_index - 1][character_index + 1] == XMAS[2] and lines[line_index + 1][character_index - 1] == XMAS[
        0]:
        found_north_east_south_west = True
    else:
        return 0

    if found_north_west_south_east and found_north_east_south_west:
        return 1

    return 0


def out_of_south_bounds(line_index: int, lines_length: int) -> bool:
    if line_index + OUT_OF_BOUNDS_LENGTH > lines_length:
        print("Out of south bounds")
        return True


def out_of_north_bounds(line_index: int) -> bool:
    if line_index - OUT_OF_BOUNDS_LENGTH + 1 < 0:
        print("Out of north bounds")
        return True


def out_of_east_bounds(word_index: int, line_length: int) -> bool:
    if word_index + OUT_OF_BOUNDS_LENGTH > line_length:
        print("Out of east bounds")
        return True


def out_of_west_bounds(word_index: int) -> bool:
    if word_index - OUT_OF_BOUNDS_LENGTH + 1 < 0:
        print("Out of west bounds")
        return True


if __name__ == "__main__":
    main()
