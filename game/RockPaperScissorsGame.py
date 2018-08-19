from random import randint
from GameInputException import GameInputException


class RockPaperScissors:
    # -1 if player1 loses
    # 0 if players tie
    # 1 if player1 wins
    def judge(self, player1, player2):
        if self.is_valid_input(player1) and self.is_valid_input(player2):
            if player1 == player2:
                return 0
            if player1 == 'R':
                if player2 == 'S':
                    return 1
                else:
                    return -1
            if player1 == 'P':
                if player2 == 'R':
                    return 1
                else:
                    return -1
            if player1 == 'S':
                if player2 == 'P':
                    return 1
                else:
                    return -1
        else:
            raise GameInputException("Invalid Input. Please try again.\n")

    @staticmethod
    def generate_input():
        random = randint(1, 3)
        if random == 1:
            return 'R'
        elif random == 2:
            return 'P'
        else:
            return 'S'

    @staticmethod
    def is_valid_input(a):
        return a != '' and a in "RPS"
