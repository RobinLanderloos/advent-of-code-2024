XMAS = "XMAS"
XMAS_LENGTH = len(XMAS)


def main():
    # file_object = open("./example-input.txt", "r")
    file_object = open("./input.txt", "r")

    lines = file_object.readlines()

    total = 0

    for line_index in range(len(lines)):
        line = lines[line_index]
        for i in range(len(line)):
            if line[i] == XMAS[0]:
                total += west_search(line, i)
                total += east_search(line, i)
                total += north_search(lines, i, line_index)
                total += south_search(lines, i, line_index)
                total += north_east_search(lines, i, line_index)
                total += north_west_search(lines, i, line_index)
                total += south_east_search(lines, i, line_index)
                total += south_west_search(lines, i, line_index)

    print(f"Total: {total}")


def out_of_south_bounds(line_index: int, lines_length: int) -> bool:
    if line_index + XMAS_LENGTH > lines_length:
        return True


def south_search(lines: [str], word_index: int, line_index: int) -> int:
    if out_of_south_bounds(line_index, len(lines)):
        return 0

    # Perform south search
    for j in range(0, XMAS_LENGTH):
        if lines[line_index + j][word_index] != XMAS[j]:
            return 0
    return 1

def south_east_search(lines: [str], word_index: int, line_index: int) -> int:
    if out_of_south_bounds(line_index, len(lines)) or out_of_east_bounds(word_index, len(lines[0])):
        return 0

    # Perform south-east search
    for i in range(0, XMAS_LENGTH):
        if lines[line_index + i][word_index + i] != XMAS[i]:
            return 0
    return 1

def south_west_search(lines: [str], word_index: int, line_index: int) -> int:
    if out_of_south_bounds(line_index, len(lines)) or out_of_west_bounds(word_index):
        return 0

    # Perform south-west search
    for i in range(0, XMAS_LENGTH):
        if lines[line_index + i][word_index - i] != XMAS[i]:
            return 0

    return 1

def out_of_north_bounds(line_index: int) -> bool:
    if line_index - XMAS_LENGTH + 1 < 0:
        return True


def north_search(lines: [str], word_index: int, line_index: int) -> int:
    if out_of_north_bounds(line_index):
        return 0

    # Perform north search
    for j in range(0, XMAS_LENGTH):
        if lines[line_index - j][word_index] != XMAS[j]:
            return 0
    return 1


def north_east_search(lines: [str], word_index: int, line_index: int) -> int:
    if out_of_north_bounds(line_index) or out_of_east_bounds(word_index, len(lines[0])):
        return 0

    # Perform north-east search
    for i in range(0, XMAS_LENGTH):
        if lines[line_index - i][word_index + i] != XMAS[i]:
            return 0
    return 1

def north_west_search(lines: [str], word_index: int, line_index: int) -> int:
    if out_of_north_bounds(line_index) or out_of_west_bounds(word_index):
        return 0

    # Perform north-west search
    for i in range(0, XMAS_LENGTH):
        if lines[line_index - i][word_index - i] != XMAS[i]:
            return 0

    return 1

def out_of_east_bounds(word_index: int, line_length: int) -> bool:
    if word_index + XMAS_LENGTH > line_length:
        return True


def east_search(line: str, index: int) -> int:
    if out_of_east_bounds(index, len(line)):
        return 0

    # Perform forwards search
    for i in range(index, index + XMAS_LENGTH - 1):
        for j in range(0, XMAS_LENGTH):
            if line[i + j] != XMAS[j]:
                return 0
        return 1


def out_of_west_bounds(word_index: int) -> bool:
    if word_index - XMAS_LENGTH + 1 < 0:
        return True


def west_search(line: str, index: int) -> int:
    if out_of_west_bounds(index):
        return 0

    # Perform backwards search
    for i in range(index, index - 1 - XMAS_LENGTH, -1):
        for j in range(0, XMAS_LENGTH):
            if line[i - j] != XMAS[j]:
                return 0
        return 1


if __name__ == "__main__":
    main()
