def main():
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

    for index in range(0, len(reports)):
        is_safe = is_report_safe(reports[index])
        # Remove unsafe level, and try again while removing the current level
        if not is_safe:
            for level_index in range(0, len(reports[index])):
                # Instead of copying and removing the level, we could just add a "skip" parameter to the is_report_safe function, but don't want to implement that now
                report_copy = reports[index].copy()
                report_copy.pop(level_index)
                is_safe = is_report_safe(report_copy)
                if is_safe:
                    break

        if is_safe:
            safe_count += 1

        if not is_safe:
            print(f"Unsafe report: {reports[index]}")

    print(f"Safe reports: {safe_count}")

def is_report_safe(report):
    is_safe = True
    is_increasing = True
    if report[0] > report[1]:
        is_increasing = False

    for index in range(0, len(report) - 1):
        if is_increasing:
            if report[index] > report[index + 1]:
                is_safe = False
                break
        else:
            if report[index] < report[index + 1]:
                is_safe = False
                break
        abs_diff = abs(report[index] - report[index + 1])
        if abs_diff < 1 or abs_diff > 3:
            is_safe = False
            break

    return is_safe

if __name__ == "__main__":
    main()
