cubes_per_game_map = {}

cubes_per_game_map = {}

with open("advent_2_input.txt", "r") as file:
    for line in file:
        id = int(line.split("Game ")[1].split(":")[0])
        grabs = line.split(": ")[1]
        for grab in grabs.split("; "):
            for color in ["blue", "red", "green"]:
                if color in grab:
                    parse_color = grab.split(f" {color}")[0]
                    value = (
                        parse_color.split(", ")[-1]
                        if "," in parse_color
                        else parse_color
                    )
                    if id in cubes_per_game_map:
                        cubes_per_game_map[id][color] += "," + value if value else ""
                    else:
                        cubes_per_game_map[id] = {"blue": "0", "red": "0", "green": "0"}
                        cubes_per_game_map[id][color] = value

thresholds = {"blue": 14, "red": 12, "green": 13}
for id in list(cubes_per_game_map.keys()):
    if any(
        int(value) > thresholds[color]
        for color in ["blue", "red", "green"]
        for value in cubes_per_game_map[id][color].split(",")
        if value
    ):
        cubes_per_game_map.pop(id)


final_sum = sum(cubes_per_game_map.keys())
print(final_sum)
