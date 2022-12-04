import string

priority_listing = {
    letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)
}

for index, letter in enumerate(string.ascii_uppercase):
    priority_listing[letter] = index + 27


def find_common_item(rucksack):
    mid = len(rucksack) // 2
    first, second = rucksack[:mid], rucksack[mid:]

    for entry in first:
        if entry in second:
            return entry


def assign_priority(item_code):
    return priority_listing[item_code]


def calc_priority_of_ruck(ruck):
    return assign_priority(find_common_item(ruck))


def calc_sum_of_rucks(rucks: list):
    list_of_priorities = []

    list_of_priorities.extend(calc_priority_of_ruck(ruck) for ruck in rucks)

    return sum(list_of_priorities)


def find_badge_item(three_rucks: list):
    for char in three_rucks[0]:
        if char in three_rucks[1] and char in three_rucks[2]:
            return char


def sum_of_badges(rucks: list):
    sublisted = divide_chunks(rucks, 3)
    badge_values = []
    for ruck_set in sublisted:
        badge = find_badge_item(ruck_set)
        priority = assign_priority(badge)
        badge_values.append(priority)
    # badge_values.extend(assign_priority(find_badge_item(set)) for set in sublisted)
    return sum(badge_values)


def divide_chunks(l: list, n: int):

    # looping till length l
    for i in range(0, len(l), n):
        yield l[i : i + n]


def main():
    filename = "day3\\inventory_list"

    with open(filename, "r", encoding="utf-8") as file:
        ruck_list = file.readlines()

    sum_of_priorities = calc_sum_of_rucks(ruck_list)

    print(sum_of_priorities)
    sum_of_badge_priorities = sum_of_badges(ruck_list)
    print(sum_of_badge_priorities)


if __name__ == "__main__":
    main()
