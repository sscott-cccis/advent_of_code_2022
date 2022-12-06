def find_first_marker(buffer: str):
    running_set = []
    for i, v in enumerate(buffer):
        running_set.append(v)
        if len(running_set) > 13:
            if not contains_repeats(running_set):
                return i + 1
            running_set.pop(0)


def contains_repeats(running_set: str):
    for i, v in enumerate(running_set):
        if running_set.count(v) > 1:
            return True

    return False


def main():
    filename = "day6\\input_data"

    with open(filename, "r", encoding="utf-8") as file:
        input_data = file.readline()

    first_marker = find_first_marker(input_data)

    print(first_marker)


if __name__ == "__main__":
    main()
