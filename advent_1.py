with open("advent_1_input.txt", "r") as file:
    total = 0
    for line in file:
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