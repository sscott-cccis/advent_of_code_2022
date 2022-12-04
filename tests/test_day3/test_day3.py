from day3.day3 import (
    find_common_item,
    assign_priority,
    calc_priority_of_ruck,
    calc_sum_of_rucks,
    find_badge_item,
    sum_of_badges,
)


def test_find_common_item():
    sample = "vJrwpWtwJgWrhcsFMMfFFhFp"
    sample2 = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
    assert find_common_item(sample) == "p"
    assert find_common_item(sample2) == "L"


def test_assign_priority():
    assert assign_priority("p") == 16
    assert assign_priority("L") == 38
    assert assign_priority("P") == 42
    assert assign_priority("v") == 22


def test_calc_priority_of_ruck():
    sample = "vJrwpWtwJgWrhcsFMMfFFhFp"
    assert calc_priority_of_ruck(sample) == 16


def test_calc_sum_of_rucks():
    sample = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert calc_sum_of_rucks(sample) == 157


def test_find_badge_item():
    sample1 = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    ]
    sample2 = [
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert find_badge_item(sample1) == "r"
    assert find_badge_item(sample2) == "Z"


def test_calc_sum_of_badges():
    sample1 = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert sum_of_badges(sample1) == 70
