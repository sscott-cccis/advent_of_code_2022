from day5.day5 import parse_move, follow_command, run_all_moves, get_listing

cargo = {"1": ["Z", "N"], "2": ["M", "C", "D"], "3": ["P"]}

moves = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_parse_move():
    assert parse_move(moves[0]) == {"count": 1, "source": "2", "dest": "1"}


def test_follow_command():
    post_move_cargo = {"1": ["Z", "N", "D"], "2": ["M", "C"], "3": ["P"]}
    cargo_test = {"1": ["Z", "N"], "2": ["M", "C", "D"], "3": ["P"]}
    assert follow_command(cargo_test, parse_move(moves[0])) == post_move_cargo


def test_run_all_moves():
    final_cargo_map = {"1": ["C"], "2": ["M"], "3": ["P", "D", "N", "Z"]}
    new_cargo_map = {"1": ["Z", "N"], "2": ["M", "C", "D"], "3": ["P"]}
    new_cargo_map = run_all_moves(new_cargo_map, moves)

    assert final_cargo_map == new_cargo_map


def test_get_listing():
    expected_listing = "CMZ"
    cargo_map = {"1": ["Z", "N"], "2": ["M", "C", "D"], "3": ["P"]}
    cargo_map = run_all_moves(cargo_map, moves)

    assert get_listing(cargo_map) == expected_listing
