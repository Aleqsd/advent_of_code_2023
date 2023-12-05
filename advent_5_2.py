def almanach_to_map(lines):
    map_ranges = []
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(" ")
            map_ranges.append((int(parts[1]), int(parts[0]), int(parts[2])))
    return map_ranges


def reverse_find(location, maps):
    next_position = location
    for map in reversed(maps):
        for start, destination, length in map:
            if destination <= next_position < destination + length:
                next_position = start + (next_position - destination)
    return next_position


locations = []
maps = []
seed_map = {}

with open("advent_5_input.txt", "r") as file:
    seeds = [int(seed) for seed in next(file).split()[1:]]
    for i in range(0, len(seeds), 2):
        seed_map[i // 2] = (seeds[i], seeds[i + 1])

    lines_to_investigate = []
    for line in file:
        line = line.strip()
        if line == "":
            maps.append(almanach_to_map(lines_to_investigate))
            lines_to_investigate = []
        elif line[0].isdigit():
            lines_to_investigate.append(line)
    maps.append(almanach_to_map(lines_to_investigate))  # For the last set of lines

location_map = maps[-1]
location_map.sort(key=lambda x: x[0])

locations = []
for start, destination, length in location_map:
    for i in range(length):
        destination_to_check = reverse_find(destination + i, maps)
        if destination_to_check != destination:
            potential_seed = destination_to_check
            if any(seed[0] <= potential_seed < seed[1] for seed in seed_map.values()):
                print(destination_to_check)
                break
