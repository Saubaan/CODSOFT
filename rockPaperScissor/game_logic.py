import random


class GameLogic:

    def __init__(self, player_move, computer_move):
        self.pMove = player_move
        self.cMove = computer_move

    @staticmethod
    def computer_move():
        move = random.randrange(1, 4)
        return move

    @staticmethod
    def player_move(move):
        if move == 1:
            return 1
        elif move == 2:
            return 2
        elif move == 3:
            return 3
        else:
            return random.randrange(1, 4)

    @staticmethod
    def move_name(move):
        if move == 1:
            return "Rock"
        elif move == 2:
            return "Paper"
        elif move == 3:
            return "Scissor"

    def game_logic(self):
        if (self.cMove == 1 and self.pMove == 2) or (self.cMove == 2 and self.pMove == 3) or (
                self.cMove == 3 and self.pMove == 1):
            return 1
        elif (self.cMove == 2 and self.pMove == 1) or (self.cMove == 3 and self.pMove == 2) or (
                self.cMove == 1 and self.pMove == 3):
            return 2
        elif self.cMove == self.pMove:
            return 3

    def game_result(self, result):
        print(f'You chose {GameLogic.move_name(self.pMove)} and the computer chose {GameLogic.move_name(self.cMove)}')
        if result == 1:
            print('You win!!')
        elif result == 2:
            print('Computer wins!!')
        else:
            print("It's a draw")
