numbers_in_letters = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3hree",
    "four": "f4ur",
    "five": "f5ve",
    "six": "s6x",
    "seven": "s7ven",
    "eight": "e8ght",
    "nine": "n9ne",
}

with open("advent_1_input.txt", "r") as file:
    total = 0
    for line in file:
        for letter, number in numbers_in_letters.items():
            line = line.replace(letter, number)
        for char in line:
            if char.isdigit():
                first = int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                second = int(char)
                break 
        total += first*10 + second

    print(total)