def does_overlap(search_pair: dict):
    # if (
    #     search_pair["first"]["start"] <= search_pair["second"]["start"]
    #     and search_pair["first"]["finish"] >= search_pair["second"]["finish"]
    # ):
    #     return True
    # return (
    #     search_pair["first"]["start"] >= search_pair["second"]["start"]
    #     and search_pair["first"]["finish"] <= search_pair["second"]["finish"]
    # )

    if (
        search_pair["first"]["start"]
        <= search_pair["second"]["start"]
        <= search_pair["first"]["finish"]
    ):
        return True
    if (
        search_pair["first"]["start"]
        <= search_pair["second"]["finish"]
        <= search_pair["first"]["finish"]
    ):
        return True
    if (
        search_pair["second"]["start"]
        <= search_pair["first"]["start"]
        <= search_pair["second"]["finish"]
    ):
        return True
    return (
        search_pair["second"]["start"]
        <= search_pair["first"]["finish"]
        <= search_pair["second"]["finish"]
    )


def parse_source_into_set(source_string: str):
    source_string = source_string.replace("\n", "")
    items = source_string.split(",")
    first_items = items[0].split("-")
    first = {"start": int(first_items[0]), "finish": int(first_items[1])}
    second_items = items[1].split("-")
    second = {"start": int(second_items[0]), "finish": int(second_items[1])}
    return {"first": first, "second": second}


def count_full_overlaps(list_of_sets: list):
    count_of_overlaps = 0
    for item in list_of_sets:
        if does_overlap(item):
            count_of_overlaps = count_of_overlaps + 1
    return count_of_overlaps


def read_source_file_into_dict(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [parse_source_into_set(line) for line in file.readlines()]


def main():
    filename = "day4\\input_data"
    record_list = read_source_file_into_dict(filename)
    print(count_full_overlaps(record_list))


if __name__ == "__main__":
    main()
