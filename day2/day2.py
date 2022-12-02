scores = {"X": 0, "Y": 3, "Z": 6}
round_result = {
    "AX": 3,
    "AY": 1,
    "AZ": 2,
    "BX": 1,
    "BY": 2,
    "BZ": 3,
    "CX": 2,
    "CY": 3,
    "CZ": 1,
}


def calc_score(choices: dict):
    return (
        scores[choices["result"]]
        + round_result[f"{choices['theirs']}{choices['result']}"]
    )


def extract_round_choices(line: str):
    line = line.replace("\n", "")
    result = line.split(" ")
    return {"theirs": result[0], "result": result[1]}


def generate_choice_listing(filename: str):
    choice_listing = []
    with open(filename, "r", encoding="utf-8") as file:
        choice_listing.extend(extract_round_choices(f) for f in file.readlines())

    return choice_listing


def calc_total_score(choice_listing: list):
    running_score = 0
    for item in choice_listing:
        running_score = running_score + calc_score(item)

    return running_score


def main():
    filename = "day2\\strategy_guide"
    listing = generate_choice_listing(filename)
    score = calc_total_score(listing)
    print(score)


if __name__ == "__main__":
    main()
