import unittest


def main():
    file = open("input.txt", "r")
    puzzle_input = file.read()
    file.close()

    blinks = 25
    stones = 0
    for i in range(blinks):
        puzzle_input, stones = blink(puzzle_input)
        print(f"Blink {i + 1} of {blinks} ({stones} stones)")
    print(f"After {blinks} blinks, there are {stones} stones.")


def blink(stones: str) -> tuple[str, int]:
    output = ""
    stones = stones.split()
    stone_count = 0
    for stone_index in range(len(stones)):
        blink_str, added_stones = apply_rule(stones[stone_index])
        output += blink_str
        stone_count += added_stones
        if stone_index != len(stones) - 1:
            output += " "

    return output, stone_count

encountered_transformations = dict[str, tuple[str, int]]()
encountered_multiplications = dict[int, int]()

def apply_rule(stone: str) -> tuple[str, int]:
    if stone in encountered_transformations:
        return encountered_transformations[stone]
    stone_value = int(stone)

    if stone_value == 0:
        encountered_transformations[stone] = ("1", 1)
        return encountered_transformations[stone]

    if len(stone) % 2 == 0:
        middle = len(stone) // 2
        encountered_transformations[stone] = (f"{int(stone[:middle])} {int(stone[middle:])}", 2)
        return encountered_transformations[stone]

    encountered_transformations[stone] = (str(stone_value * 2024), 1)
    return encountered_transformations[stone]

class PlutoniumPebblesTests(unittest.TestCase):
    def test_example_inputs(self):
        test_cases = [
            ("0 1 10 99 999", 1, 7),
            ("125 17", 1, 3),
            ("125 17", 2, 4),
            ("125 17", 3, 5),
            ("125 17", 4, 9),
            ("125 17", 5, 13),
            ("125 17", 6, 22),
            ("125 17", 25, 55312),
        ]

        for case in test_cases:
            with self.subTest(case=case):
                test_input = case[0]
                print(f"Input: {test_input}")
                blinks = case[1]
                expected_stones = case[2]
                stones = 0
                for i in range(blinks):
                    test_input, stones = blink(test_input)
                    print(f"Blink {i + 1} of {blinks} ({stones} stones)")
                self.assertEqual(stones, expected_stones)


if __name__ == '__main__':
    main()
