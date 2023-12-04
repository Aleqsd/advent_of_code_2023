with open("advent_4_input.txt", "r") as file:
    lines = file.readlines()

total_sum = 0
for line in lines:
    line = line.strip()
    id = int(line.split("Card ")[1].split(":")[0].replace(" ", ""))

    winning_numbers = line.split(": ")[1].split("|")[0].split(" ")
    winning_numbers = [int(number) for number in winning_numbers if number.isdigit()]
    my_numbers = line.split("|")[1].split(" ")
    my_numbers = [int(number) for number in my_numbers if number.isdigit()]

    matching_numbers = 0
    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            matching_numbers += 1

    total_sum += id * matching_numbers

print(total_sum)
