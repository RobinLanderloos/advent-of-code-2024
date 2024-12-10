def main():
    line = open("example-input.txt").readline()
    output, empty_spaces, file_blocks = convert_input(line)
    print(output)

    defragment(file_blocks, output)



def defragment(file_blocks: dict[str, int], input_str: str) -> str:
    output = ""
    remainder = 0

    for file_block_key in reversed(file_blocks):
        print(file_block_key)
        print(file_blocks[file_block_key])

    return output


def convert_input(input_string: str) -> tuple[str, dict[int, int], dict[str, int]]:
    output = ""
    disk_id = 0
    is_empty_space = False
    empty_spaces = dict[int, int]()
    file_blocks = dict[str, int]()

    for char_index in range(len(input_string)):
        char_int = int(input_string[char_index])

        if is_empty_space:
            for i in range(char_int):
                output += "."
            empty_spaces[char_index] = char_int
            is_empty_space = False
        else:
            for i in range(char_int):
                output += str(disk_id)
            file_blocks[disk_id] = char_int
            is_empty_space = True
            disk_id += 1

    return output, empty_spaces, file_blocks


if __name__ == "__main__":
    main()
