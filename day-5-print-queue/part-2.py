﻿def main():
    file_object = open("./input.txt", "r")

    lines = file_object.readlines()

    rules, split_index = get_rules(lines)

    valid_pages, total, invalid_pages, invalid_total = get_pages(lines, split_index, rules)

    print(f"Valid Pages ({len(valid_pages)}), total ({total})")
    print(f"Invalid Pages ({len(invalid_pages)}), total ({invalid_total})")


def get_pages(lines: list[str], split_index: int, rules: dict) -> tuple[list[str], int, list[str], int]:
    valid_pages = []
    invalid_pages = []
    total = 0
    invalid_total = 0
    start_index = split_index + 1

    for line_index in range(start_index, len(lines)):
        line = lines[line_index].strip()
        print(f"Checking page {line}")
        # We won't perform rule checks on the first number of the page
        page_valid, middle_value = check_page_validity(line, rules)
        if page_valid:
            valid_pages.append(line)
            total += middle_value
        else:
            middle_value = check_page_validity_and_fix(line, rules)
            invalid_pages.append(line)
            invalid_total += middle_value

    return valid_pages, total, invalid_pages, invalid_total


def get_rules(lines: list[str]) -> tuple[dict, int]:
    rules = {}
    split_index = 0
    for lines_index in range(len(lines)):
        if lines[lines_index] == "\n":
            split_index = lines_index
            break

        split_rule = lines[lines_index].strip().split("|")

        if split_rule[1] not in rules:
            print(f"Adding rule {split_rule[1]} to rules with rule {split_rule[0]}")
            rules[split_rule[1]] = {split_rule[0]}
        else:
            print(f"Adding {split_rule[0]} to rule {split_rule[1]}")
            rules[split_rule[1]].add(split_rule[0])

    print(f"Rules ({len(rules)}):")
    print(rules)

    return rules, split_index


def check_page_validity_and_fix(line: str, rules: dict) -> int:
    numbers = line.strip().split(",")

    for number_index in range(len(numbers)):
        number = numbers[number_index]

        if number in rules:
            for number_check_index in range(number_index + 1, len(numbers)):
                number_check = numbers[number_check_index]
                if number_check in rules[number]:
                    print("-> invalid")
                    # Swap
                    numbers[number_index] = numbers[number_check_index]
                    numbers[number_check_index] = number
                    print(numbers)
                    return check_page_validity_and_fix(",".join(numbers), rules)

    print("-> valid")
    middle_number_index = int(len(numbers) / 2)
    return int(numbers[int(middle_number_index)])


def check_page_validity(line: str, rules: dict) -> tuple[bool, int]:
    numbers = line.strip().split(",")

    for number_index in range(len(numbers)):
        number = numbers[number_index]

        if number in rules:
            for number_check_index in range(number_index + 1, len(numbers)):
                number_check = numbers[number_check_index]
                if number_check in rules[number]:
                    print(f"-> invalid")
                    return False, 0

    print(f"-> valid")
    middle_number_index = int(len(numbers) / 2)
    return True, int(numbers[int(middle_number_index)])


if __name__ == "__main__":
    main()
