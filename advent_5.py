def almanach_to_map(lines):
    map_ranges = []
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(" ")
            map_ranges.append((int(parts[1]), int(parts[0]), int(parts[2])))
    return map_ranges


def find_destination(seed, map_ranges):
    next_position = seed
    for start, destination, length in map_ranges:
        if start <= next_position < start + length:
            return destination + (next_position - start)
    return next_position


locations = []
maps = []

with open("advent_5_input.txt", "r") as file:
    seeds = [int(seed) for seed in next(file).split()[1:]]

    lines_to_investigate = []
    for line in file:
        line = line.strip()
        if line == "":
            maps.append(almanach_to_map(lines_to_investigate))
            lines_to_investigate = []
        elif line[0].isdigit():
            lines_to_investigate.append(line)
    maps.append(almanach_to_map(lines_to_investigate))  # For the last set of lines

for seed in seeds:
    next_position = seed
    for map_ranges in maps:
        next_position = find_destination(next_position, map_ranges)
    locations.append(next_position)

print(min(locations))
