def main():
    file_object = open(r"./input.txt", "r")
    lines = file_object.readlines()

    left = []
    right = []

    # Split the lines into the left and right lists
    for index in range(0, len(lines)):
        print(f"Line: {index + 1}")
        split_line = lines[index].strip().split("   ")
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))

    # Sort the lists so that we can pair them up
    left.sort()
    right.sort()

    print(f"Left: {left}")
    print(f"Right: {right}")

    total_distance = 0

    # Calculate the absolute value between the two numbers and add it to the total distance
    for index in range(0, len(left)):
        print(f"Pair: {index + 1}, Left: {left[index]}, Right: {right[index]}")
        distance = abs(left[index] - right[index])
        print(f"Distance: {distance}")
        total_distance += distance

    print(total_distance)


if __name__ == "__main__":
    main()