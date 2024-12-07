import time
from itertools import product

operators = ['+', '*']


def main():
    file_object = open("./input.txt", "r")
    lines = file_object.readlines()
    file_object.close()

    operator_combinations = dict[int, list[str]]()
    total_calibration_result = 0

    for line in lines:
        result_calibration_split = line.strip().split(": ")
        result = int(result_calibration_split[0])
        calibration_split = result_calibration_split[1].split(" ")
        is_valid = is_valid_calibration(calibration_split, result, operator_combinations)
        if is_valid:
            total_calibration_result += result

    print(total_calibration_result)

def is_valid_calibration(calibrations: list[str], expected_result: int,
                         operator_combinations: dict[int, list[str]]) -> bool:
    calibration_length = len(calibrations)
    if calibration_length not in operator_combinations:
        operator_combinations[calibration_length] = get_combinations(calibration_length - 1)

    combinations = operator_combinations[calibration_length]

    for combination in combinations:
        total = int(calibrations[0])
        for i in range(len(combination)):
            calibration = int(calibrations[i + 1])
            if combination[i] == '+':
                total += calibration
            elif combination[i] == '*':
                total *= calibration
            else:
                raise ValueError("Invalid operator")

        if total == expected_result:
            return True
    return False


def get_combinations(amount: int) -> list[str]:
    combinations = []
    products = product(operators, repeat=amount)

    for comb in products:
        combination = ''.join(comb)
        combinations.append(combination)

    return combinations


if __name__ == "__main__":
    main()
