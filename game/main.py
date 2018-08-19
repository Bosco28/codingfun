from RockPaperScissorsGame import RockPaperScissors
from GameInputException import GameInputException


def get_full_name(a):
    inputmap = {'R': "Rock", 'P': "Paper", 'S': "Scissors"}
    if RockPaperScissors.is_valid_input(a):
        return inputmap[a]
    else:
        return a


if __name__ == '__main__':
    game = RockPaperScissors()
    print("This is a rock paper scissors game.")
    while True:
        action = input("Play [R]ock, [P]aper, [S]cissors or [Q]uit\n").upper()
        if action == 'Q':
            print("Bye")
            quit(0)
        else:
            try:
                computer = game.generate_input()
                print("Your input: " + get_full_name(action))
                print("Computer input: " + get_full_name(computer))
                result = game.judge(action, computer)
                if result == 1:
                    print("You won!\n")
                elif result == -1:
                    print("You lost!\n")
                else:
                    print("You tied!\n")
            except GameInputException as e:
                print(str(e))
