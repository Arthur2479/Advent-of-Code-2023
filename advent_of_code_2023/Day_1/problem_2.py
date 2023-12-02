"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two,
three, four, five, six, seven, eight, and nine also count as valid "digits".
Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

import re
from pathlib import Path

INPUT_FILE_PATH = Path('./input.txt')
TEST_FILE_PATH = Path('./test_values_2.txt')

digits_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def str_to_int(input_digits: tuple[str, ...]) -> list[int, int]:
    output_digits = []
    for i, digit in enumerate(input_digits):
        if digit.isdigit():
            output_digits.append(int(digit))
            continue

        output_digits.append(digits_map[digit])

    return output_digits


def find_digits(line: str) -> list[int, int]:
    # Regex used : https://regex101.com/r/p3TYiB/2. Matches all occurrences of digits (str or int)
    m: list[str] = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)

    return str_to_int((m[0], m[-1]))


def sum_of_digits_calibration_values_with_spelled_digits(file_path: Path):
    with open(file_path) as file:
        calibration_values = []
        while line := file.readline()[:-1]:
            first, last = find_digits(line)
            calibration_values.append(10 * first + last)

        print(f'Sum of calibration values : {sum(calibration_values)}')


if __name__ == '__main__':
    sum_of_digits_calibration_values_with_spelled_digits(file_path=INPUT_FILE_PATH)
