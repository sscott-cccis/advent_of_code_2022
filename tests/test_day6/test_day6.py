from day6.day6 import contains_repeats, find_first_marker

samples = [
    {"input": "mjqjpqmgbljsphdztnvjfqwrcgsmlb", "expected": 19},
    {"input": "bvwbjplbgvbhsrlpgdmjqwftvncz", "expected": 23},
    {"input": "nppdvjthqldpwncqszvftbrmjlhg", "expected": 23},
    {"input": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "expected": 29},
    {"input": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "expected": 26},
]


def test_contains_repeats():
    sample1 = "mjqj"
    sample2 = "jpqm"

    assert contains_repeats(sample1)
    assert contains_repeats(sample2) is False


def test_find_first_marker():
    for sample in samples:
        assert find_first_marker(sample["input"]) == sample["expected"]
