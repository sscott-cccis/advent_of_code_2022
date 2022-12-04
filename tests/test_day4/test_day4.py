from day4.day4 import (
    does_overlap,
    parse_source_into_set,
    count_full_overlaps,
    read_source_file_into_dict,
)

sample_set = [
    {"first": {"start": 2, "finish": 4}, "second": {"start": 6, "finish": 8}},
    {"first": {"start": 2, "finish": 3}, "second": {"start": 4, "finish": 5}},
    {"first": {"start": 5, "finish": 7}, "second": {"start": 7, "finish": 9}},
    {"first": {"start": 2, "finish": 8}, "second": {"start": 3, "finish": 7}},
    {"first": {"start": 6, "finish": 6}, "second": {"start": 4, "finish": 6}},
    {"first": {"start": 2, "finish": 6}, "second": {"start": 4, "finish": 8}},
]

source_sample = "2-4,6-8\n"


def test_fully_overlapping_sets_return_true():
    assert does_overlap(sample_set[3])
    assert does_overlap(sample_set[4])


def test_partially_overlapping_sets_return_true():
    assert does_overlap(sample_set[5]) == True


def test_nonoverlapping_sets_return_false():
    assert does_overlap(sample_set[0]) == False


def test_parse_source_into_set():
    assert parse_source_into_set(source_sample) == sample_set[0]


def test_count_full_overlaps():
    assert count_full_overlaps(sample_set) == 4


def test_read_source_file_into_dict():
    filename = "tests\\test_day4\\sample_data"
    assert read_source_file_into_dict(filename) == sample_set
