def main():
    line = open("example-input.txt").readline()
    output, empty_spaces, file_blocks = convert_input(line)
    print(output)

    print(defragment(file_blocks, output))



def defragment(file_blocks: dict[str, int], input_str: str) -> str:
    output = ""
    remainder = 0

    str_ptr = 0
    encountered_keys = set()
    for file_block_key in reversed(file_blocks):
        print(f"Checking key {file_block_key}, encountered keys: {encountered_keys}")
        if file_block_key in encountered_keys:
            print(f"Duplicate key {file_block_key} found")
            continue

        if file_block_key == 0:
            continue

        remaining_file_blocks = file_blocks[file_block_key]

        while remaining_file_blocks > 0:

            if str_ptr >= len(input_str):
                return output

            if input_str[str_ptr] == ".":
                output += str(file_block_key)
                remaining_file_blocks -= 1
                remainder += 1
            else:
                print(f"Adding key {file_block_key}")
                encountered_keys.add(file_block_key)
                output += input_str[str_ptr]
            str_ptr += 1


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
