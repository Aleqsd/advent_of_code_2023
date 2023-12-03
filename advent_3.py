def check_surrounding(lines, line_index, char_index, number_of_digits) -> bool:
    lines_to_check = []
    if line_index > 0:
        lines_to_check.append(lines[line_index - 1])
    lines_to_check.append(lines[line_index])
    if line_index < len(lines) - 1:
        lines_to_check.append(lines[line_index + 1])

    for line_to_check in lines_to_check:
        for digit in range(number_of_digits):
            for offset in [-1, 0, 1]:
                check_index = char_index + digit + offset
                if 0 <= check_index < len(line_to_check):
                    if (
                        not line_to_check[check_index].isdigit()
                        and line_to_check[check_index] != "."
                        and line_to_check[check_index] != "\n"
                        and line_to_check[check_index] != "\r"
                    ):
                        return True
    return False


sum = 0
with open("advent_3_input.txt", "r") as file:
    lines = file.readlines()

for line_index, line in enumerate(lines):
    char_index = 0
    while char_index < len(line):
        if line[char_index].isdigit():
            number = int(line[char_index])
            number_of_digits = 1
            start_index = char_index
            char_index += 1
            while char_index < len(line) and line[char_index].isdigit():
                number = number * 10 + int(line[char_index])
                number_of_digits += 1
                char_index += 1
            if check_surrounding(
                lines,
                line_index,
                start_index,
                number_of_digits,
            ):
                sum += number
        else:
            char_index += 1

print(sum)
