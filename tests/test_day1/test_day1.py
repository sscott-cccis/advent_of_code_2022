from day1.day1 import (
    count_calories,
    find_highest_total,
    import_data,
    find_sum_of_top_three,
)


def test_count_calories_returns_correct_sum_for_integers():
    sample = [7000, 8000, 9000]
    assert count_calories(sample) == 24000


def test_find_highest_total_returns_highest_sum():
    sample = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    assert find_highest_total(sample) == 24000


def test_find_sum_of_top_three():
    sample = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    assert find_sum_of_top_three(sample) == 45000


def test_import_data():
    sample = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    with open(
        "C:\\Users\\sscott\\OneDrive - CCC Intelligent Solutions Inc\\Documents\\github repos\\advent_of_code_2022\\tests\\test_day1\\sample_data.txt",
        "r",
        encoding="utf-8",
    ) as file:
        raw_lines = file.readlines()

        assert import_data(raw_lines) == sample


def test_end_to_end():
    with open(
        "C:\\Users\\sscott\\OneDrive - CCC Intelligent Solutions Inc\\Documents\\github repos\\advent_of_code_2022\\tests\\test_day1\\sample_data.txt",
        "r",
        encoding="utf-8",
    ) as file:
        raw_lines = file.readlines()
        sample = import_data(raw_lines)
        assert find_highest_total(sample) == 24000
