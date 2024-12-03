import re

mul_pattern = r"(mul\(\d+,\d+\))"
operator_pattern = r".+(?=\()"
left_digit_pattern = r"\d+(?=\,)"
right_digit_pattern = r"\d+(?=\))"

def main():
    file_object = open("./input.txt", "r")

    lines = file_object.readlines()

    total = 0

    for line in lines:
        matches = re.findall(mul_pattern, line)
        print(matches)
        for match in matches:
            left = re.findall(left_digit_pattern, match)[0]
            right = re.findall(right_digit_pattern, match)[0]
            total += int(left) * int(right)

    print(f"Total: {total}")

if __name__ == "__main__":
    main()