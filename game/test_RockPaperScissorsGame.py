from RockPaperScissorsGame import RockPaperScissors
from GameInputException import GameInputException
import pytest

invalid_input1 = 'A'
invalid_input2 = 'ABC'

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
    assert not game.is_valid_input(invalid_input1)


def test_check_input_invalid_word():
    game = RockPaperScissors()
    assert not game.is_valid_input(invalid_input2)

# Testing generate_input
# ================================================================


def test_generate_valid_input():
    game = RockPaperScissors()
    for _ in range(100):
        assert game.is_valid_input(game.generate_input())

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
        game.judge('', 'R')
    pass


def test_empty_second_input():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge('R', '')
    pass


def test_empty_both_inputs():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge('', '')
    pass


def test_invalid_first_input_character():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge(invalid_input1, '')
    pass


def test_invalid_first_input_word():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge(invalid_input2, '')
    pass


def test_invalid_second_input_character():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge('', invalid_input1)
    pass


def test_invalid_second_input_word():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge('', invalid_input2)
    pass


def test_invalid_both_inputs_character():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge(invalid_input1, invalid_input1)
    pass


def test_invalid_both_inputs_word():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge(invalid_input2, invalid_input2)
    pass


def test_invalid_both_inputs_word_character():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge(invalid_input2, invalid_input1)
    pass


def test_invalid_both_inputs_character_word():
    with pytest.raises(GameInputException, message="Invalid Input. Please try again.\n"):
        game = RockPaperScissors()
        game.judge(invalid_input1, invalid_input2)
    pass
