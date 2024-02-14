from game_logic import GameLogic

while True:
    print('____________________________________________________________')
    x = int(input("1. Rock\n2. Paper\n3. Scissor\nEnter your move:"))
    G = GameLogic(player_move=GameLogic.player_move(x), computer_move=GameLogic.computer_move())
    G.game_result(G.game_logic())
    print('____________________________________________________________')
    play_again = int(input("1. Play again\t2. Quit :"))
    if play_again == 2:
        break
    else:
        continue

