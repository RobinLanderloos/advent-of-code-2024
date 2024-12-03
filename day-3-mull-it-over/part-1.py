import re

mul_pattern = r"(mul\(\d+,\d+\))"
operator_pattern = r".+(?=\()"
left_digit_pattern = r"\d+(?=\,)"
right_digit_pattern = r"\d+(?=\))"

def main():
    file_object = open("./input.txt", "r")

    lines = file_object.readlines()

    total = 0

    print(lines)

    for line in lines:
        matches = re.findall(mul_pattern, line)
        print(matches)
        for match in matches:
            operator = re.findall(operator_pattern, match)[0]
            print(operator)
            left = re.findall(left_digit_pattern, match)[0]
            print(left)
            right = re.findall(right_digit_pattern, match)[0]
            print(right)
            total += int(left) * int(right)

    print(f"Total: {total}")

if __name__ == "__main__":
    main()