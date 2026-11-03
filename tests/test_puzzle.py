from nonogram.puzzle import parse_clues, print_grid


def test_parse_clues():
    assert parse_clues('"1,1","1","2,3"') == [
        [1, 1],
        [1],
        [2, 3],
    ]


def test_parse_single_clue():
    assert parse_clues('"3"') == [[3]]


def test_print_grid(capsys):
    grid = [
        [2, 1],
        [1, 2],
    ]

    print_grid(grid)

    captured = capsys.readouterr()

    assert captured.out == "* \n *\n"