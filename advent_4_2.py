with open("advent_4_input.txt", "r") as file:
    lines = file.readlines()

card_map = {}
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

    matching_number_map = []

    for matching_number in range(matching_numbers):
        matching_number_map.append(matching_number + id + 1)
    card_map[id] = [matching_number_map]
    card_map[id].append([id])

    # Ugly and super slow but it works
    # Probably infinitely faster if instead of repeating the array,
    # we use a counter. But I don't have enough time lol
    for card_map_id, card_numbers_lists in card_map.items():
        if card_map_id < id:
            for card_numbers_list in card_numbers_lists:
                if id in card_numbers_list:
                    new_matching_number_map = [
                        matching_number + id + 1
                        for matching_number in range(matching_numbers)
                    ]
                    card_map[id].append(new_matching_number_map)

for _, card_numbers_lists in card_map.items():
    for card_numbers_list in card_numbers_lists:
        for card_number in card_numbers_list:
            total_sum += 1


print(total_sum)
