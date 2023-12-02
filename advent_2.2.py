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
                        cubes_per_game_map[id][color] += "," + value if value else "0"
                    else:
                        cubes_per_game_map[id] = {"blue": "0", "red": "0", "green": "0"}
                        cubes_per_game_map[id][color] = value

final_min_sum = 0
for id in cubes_per_game_map.keys():
    max_blue = max(
        int(value) for value in cubes_per_game_map[id]["blue"].split(",") if value
    )
    max_red = max(
        int(value) for value in cubes_per_game_map[id]["red"].split(",") if value
    )
    max_green = max(
        int(value) for value in cubes_per_game_map[id]["green"].split(",") if value
    )
    final_min_sum += max_blue * max_red * max_green

print(final_min_sum)
