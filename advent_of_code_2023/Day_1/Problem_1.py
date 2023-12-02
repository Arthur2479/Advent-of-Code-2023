"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit
and the last digit (in that order) to form a single two-digit number. For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""


def sum_of_digits_calibration_values():
    with open('./input.txt') as file:
        calibration_values = []
        while line := file.readline():
            first = last = ''
            for char in line:
                if char.isdigit():
                    if not first:
                        first = char
                    last = char
            calibration_values.append(int(first + last))

        print(f'Sum of calibration values : {sum(calibration_values)}')


if __name__ == '__main__':
    sum_of_digits_calibration_values()
