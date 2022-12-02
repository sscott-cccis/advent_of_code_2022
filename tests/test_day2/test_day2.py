from day2.day2 import (
    calc_score,
    extract_round_choices,
    generate_choice_listing,
    calc_total_score,
)

choice_list = [
    {"theirs": "A", "result": "Y"},
    {"theirs": "B", "result": "X"},
    {"theirs": "C", "result": "Z"},
]


def test_calc_score_returns_correct_value():
    sample1 = {"theirs": "B", "result": "X"}
    sample2 = {"theirs": "C", "result": "Z"}
    sample3 = {"theirs": "A", "result": "Y"}

    assert calc_score(sample1) == 1
    assert calc_score(sample2) == 7
    assert calc_score(sample3) == 4


def test_extract_round_choices():
    sample = "A Y\n"
    sample2 = "A Y"
    expected_result = {"theirs": "A", "result": "Y"}
    assert extract_round_choices(sample) == expected_result
    assert extract_round_choices(sample2) == expected_result


def test_generate_choice_listing():
    filename = "tests\\test_day2\\sample_data"

    assert generate_choice_listing(filename) == choice_list


def test_calc_total_score():
    assert calc_total_score(choice_list) == 12
