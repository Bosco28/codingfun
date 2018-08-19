from RockPaperScissorsGame import RockPaperScissors
from GameInputException import GameInputException
import pytest

# Testing is_valid_input
# ================================================================


def test_check_input_rock():
    game = RockPaperScissors()
    assert game.is_valid_input('R')


def test_check_input_paper():
    game = RockPaperScissors()
    assert game.is_valid_input('P')


def test_check_input_scissors():
    game = RockPaperScissors()
    assert game.is_valid_input('S')


def test_check_input_empty():
    game = RockPaperScissors()
    assert not game.is_valid_input('')


def test_check_input_invalid_character():
    game = RockPaperScissors()
    for c in range(128):
        char = chr(c).upper()
        if char not in "RPS":
            assert not game.is_valid_input(char)

# Testing generate_input
# ================================================================


def test_generate_valid_input():
    game = RockPaperScissors()
    freq = {'R': False, 'P': False, 'S': False}
    for _ in range(1000):
        i = game.generate_input()
        assert game.is_valid_input(i)
        freq[i] = True
    assert freq['R']
    assert freq['P']
    assert freq['S']

# Testing judge
# ================================================================


def test_rock_rock():
    game = RockPaperScissors()
    assert game.judge('R', 'R') == 0


def test_rock_paper():
    game = RockPaperScissors()
    assert game.judge('R', 'P') == -1


def test_rock_scissors():
    game = RockPaperScissors()
    assert game.judge('R', 'S') == 1


def test_paper_rock():
    game = RockPaperScissors()
    assert game.judge('P', 'R') == 1


def test_paper_paper():
    game = RockPaperScissors()
    assert game.judge('P', 'P') == 0


def test_paper_scissors():
    game = RockPaperScissors()
    assert game.judge('P', 'S') == -1


def test_scissors_rock():
    game = RockPaperScissors()
    assert game.judge('S', 'R') == -1


def test_scissors_paper():
    game = RockPaperScissors()
    assert game.judge('S', 'P') == 1


def test_scissors_scissors():
    game = RockPaperScissors()
    assert game.judge('S', 'S') == 0


def test_empty_first_input():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        for i in "RPS":
            game.judge('', i)
    pass


def test_empty_second_input():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        for i in "RPS":
            game.judge(i, '')
    pass


def test_empty_both_inputs():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge('', '')
    pass


def test_invalid_first_input_character():
    game = RockPaperScissors()
    for c in range(128):
        char = chr(c).upper()
        if char not in "RPS":
            for i in "RPS":
                with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
                    game.judge(char, i)
    pass


def test_invalid_second_input_character():
    game = RockPaperScissors()
    for c in range(128):
        char = chr(c).upper()
        if char not in "RPS":
            for i in "RPS":
                with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
                    game.judge(i, char)
    pass
