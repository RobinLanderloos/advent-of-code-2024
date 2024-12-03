import re

do_matches_pattern = r"((do\(\)|^).*?(?:don't\(\)|$))"
mul_pattern = r"(mul\(\d+,\d+\))"
left_digit_pattern = r"\d+(?=\,)"
right_digit_pattern = r"\d+(?=\))"

def main():
    file_object = open("./input.txt", "r")

    lines = file_object.readlines()

    # We expect a single line of input
    line = lines[0]

    total = 0

    do_matches = re.findall(do_matches_pattern, line, re.RegexFlag.MULTILINE)
    for match in do_matches:
        print(match)
        mul_matches = re.findall(mul_pattern, match[0])
        for mul_match in mul_matches:
            print(mul_match)
            left = re.findall(left_digit_pattern, mul_match)[0]
            right = re.findall(right_digit_pattern, mul_match)[0]
            total += int(left) * int(right)

    print(f"Total: {total}")

if __name__ == "__main__":
    main()
