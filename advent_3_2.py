def check_surrounding(lines, line_index, char_index, number_of_digits):
    lines_to_check = {}
    if line_index > 0:
        lines_to_check[line_index - 1] = lines[line_index - 1]
    lines_to_check[line_index] = lines[line_index]
    if line_index < len(lines) - 1:
        lines_to_check[line_index + 1] = lines[line_index + 1]

    for checked_line_index, line_to_check in lines_to_check.items():
        for offset in range(-1, number_of_digits + 1):
            check_index = char_index + offset
            if (
                0 <= check_index < len(line_to_check)
                and line_to_check[check_index] == "*"
            ):
                return checked_line_index, check_index
    return 0, 0


with open("advent_3_input.txt", "r") as file:
    lines = file.readlines()

map_star_numbers = {}
for line_index, line in enumerate(lines):
    char_index = 0
    while char_index < len(line):
        if line[char_index].isdigit():
            start_index = char_index
            while char_index < len(line) and line[char_index].isdigit():
                char_index += 1
            number = int(line[start_index:char_index])
            number_of_digits = char_index - start_index

            star_line_index, star_char_index = check_surrounding(
                lines,
                line_index,
                start_index,
                number_of_digits,
            )
            if star_line_index != 0 and star_char_index != 0:
                map_star_numbers.setdefault(
                    (star_line_index, star_char_index), set()
                ).add(number)
        else:
            char_index += 1

final_sum = 0
for star_line_index, star_char_index in map_star_numbers.keys():
    if len(map_star_numbers[(star_line_index, star_char_index)]) == 2:
        final_sum += min(map_star_numbers[(star_line_index, star_char_index)]) * max(
            map_star_numbers[(star_line_index, star_char_index)]
        )


print(final_sum)
