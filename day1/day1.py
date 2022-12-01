def count_calories(calories_carried: list):
    return sum(calories_carried)


def find_highest_total(calorie_inventory: list):
    highest = 0
    for set_of_entries in calorie_inventory:
        current = count_calories(set_of_entries)
        if current > highest:
            highest = current
    return highest


def find_sum_of_top_three(calorie_inventory: list):
    sum_list = [count_calories(item) for item in calorie_inventory]
    sum_list.sort(reverse=True)
    top_three = sum_list[:3]
    return count_calories(top_three)


def import_data(raw_lines: list[str]):
    data = []
    elf = []
    for line in raw_lines:
        line = line.replace("\n", "")
        if line == "":
            data.append(elf)
            elf = []
            continue
        elf.append(int(line))
    data.append(elf)
    return data


def main():
    with open(
        "day1\\data_set.txt",
        "r",
        encoding="utf-8",
    ) as file:
        raw_lines = file.readlines()
        data_set = import_data(raw_lines)

        print(find_highest_total(data_set))
        print(find_sum_of_top_three(data_set))


if __name__ == "__main__":
    main()
