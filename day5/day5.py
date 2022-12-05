starting_cargo_map = {
    "1": ["B", "Q", "C"],
    "2": ["R", "Q", "W", "Z"],
    "3": ["B", "M", "R", "L", "V"],
    "4": ["C", "Z", "H", "V", "T", "W"],
    "5": ["D", "Z", "H", "B", "N", "V", "G"],
    "6": ["H", "N", "P", "C", "J", "F", "V", "Q"],
    "7": ["D", "G", "T", "R", "W", "Z", "S"],
    "8": ["C", "G", "M", "N", "B", "W", "Z", "P"],
    "9": ["N", "J", "B", "M", "W", "Q", "F", "P"],
}


def parse_move(raw_move: str):
    raw_move = raw_move.replace("\n", "")
    tokens = raw_move.split(" ")
    return {"count": int(tokens[1]), "source": tokens[3], "dest": tokens[5]}


def follow_command(cargo: dict, move: dict):
    storage = []
    for _ in range(move["count"]):
        storage.append(cargo[move["source"]].pop())
    for _ in range(len(storage)):
        cargo[move["dest"]].append(storage.pop())
    return cargo


def run_all_moves(cargo, moves):
    for move in moves:
        new_cargo_map = cargo
        new_cargo_map = follow_command(new_cargo_map, parse_move(move))
    return new_cargo_map


def get_listing(cargo_map):
    listing = ""
    for key in cargo_map.keys():
        listing = f"{listing}{cargo_map[key][-1]}"
    return listing


# {"count": 1, "source": "2", "dest": "1"}
# cargo = {"1": ["Z", "N"], "2": ["M", "C", "D"], "3": ["P"]}


def main():
    with open("day5\\moves_list", "r", encoding="utf-8") as file:
        moves_list = file.readlines()

    new_cargo_map = run_all_moves(starting_cargo_map, moves_list)
    listing = get_listing(new_cargo_map)

    print(listing)


if __name__ == "__main__":
    main()
