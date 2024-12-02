def main():
    # Report = a line in the input file
    # Every number is a level, separated by spaces

    # A report is only safe as
    # - The levels are either all increasing or all decreasing.
    # - Any two adjacent levels differ by at least one and at most three.

    file_object = open("./input.txt", "r")

    lines = file_object.readlines()

    # We collect the reports first, we could perform the checks on the reports as we collect them, but it's easier and more readable to do it afterward
    reports = []
    for line in lines:
        report = []
        for level in line.strip().split(" "):
            report.append(int(level))
        reports.append(report)

    safe_count = 0

    for report in reports:
        is_safe = True
        is_increasing = True
        if report[0] > report[1]:
            is_increasing = False

        # TODO: Man, this is some ugly code, refactor
        for index in range(0, len(report) - 1):
            if is_increasing:
                if report[index] > report[index + 1]:
                    is_safe = False
                    break
                else:
                    abs_diff = abs(report[index] - report[index + 1])
                    if abs_diff < 1 or abs_diff > 3:
                        is_safe = False
                        break
            else:
                if report[index] < report[index + 1]:
                    is_safe = False
                    break
                else:
                    abs_diff = abs(report[index] - report[index + 1])
                    if abs_diff < 1 or abs_diff > 3:
                        is_safe = False
                        break

        print(f"Report: {report} safe? {is_safe}")
        if is_safe:
            safe_count += 1

    print(f"Safe reports: {safe_count}")



if __name__ == "__main__":
    main()