def main():
    file_object = open(r"./input.txt", "r")
    lines = file_object.readlines()

    left = []
    right = []

    for index in range(0, len(lines)):
        print(f"Line: {index + 1}")
        split_line = lines[index].strip().split("   ")
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))

    print(f"Left: {left}")
    print(f"Right: {right}")

    right_dict = {}
    for index in range(0, len(right)):
        if right[index] in right_dict:
            right_dict[right[index]] += 1
        else:
            right_dict[right[index]] = 1

    print(f"Right Dict: {right_dict}")
    
    simularity_score = 0

    for index in range(0, len(left)):
        if left[index] in right_dict:
            score = left[index] * right_dict[left[index]]
            print(f"Left: {left[index]}, Right: {right_dict[left[index]]}, Score: {score}")
            simularity_score += score
        else:
            print(f"Left: {left[index]}, Right: 0, Score: 0")

    print(simularity_score)


if __name__ == "__main__":
    main()