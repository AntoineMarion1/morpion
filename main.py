import argparse

from board import Board




if __name__ == '__main__': 

    parser = argparse.ArgumentParser()
    parser.add_argument("nbplayers", 
                        help= "1 or 2", 
                        type = str)

    args = parser.parse_args()
    nb_players = args.nbplayers

    board = Board()

    if nb_players == "1": 
        start = ""
        while start != "y" and start != "n": 
            start = input("\nDo you want to start playing ? (y/n) ")
            if start == "y": 
                computer_player = -1
            elif start == "n": 
                computer_player = 1
        


        end = False 
        while end == False: 

            board.compute_player()

            valid_move = False 

            if board.player == computer_player:
                print("The computer is trying to find the best move for player " + str(computer_player))
                coo_x, coo_y = board.compute_best_move()
                valid_move = board.play_a_move((coo_x, coo_y))

            else: 
                coo_x = input("\nx coo for the player " + str(board.player) + ": ")
                coo_y = input("y coo for the player " + str(board.player) + ": ")
                valid_move = board.play_a_move((coo_x, coo_y))

                while valid_move == False:
                    print("The coordinates you have provided are invalid. Please try again.")
                    coo_x = input("x coo for the player " + str(board.player) + ": ")
                    coo_y = input("y coo for the player " + str(board.player) + ": ")
                    valid_move = board.play_a_move((coo_x, coo_y))


            board.compute_winner()
            if  board.winner != 0 or board.grid.all() == True: 
                end = True

            board.terminal_display()

        if  board.winner != 0: 
            print("The winner is the player " + str(board.winner))
        else: 
            print("Draw")




    elif nb_players == "2": 

        end = False 
        while end == False: 
            board.compute_player()

            valid_move = False 
            coo_x = input("\nx coo for the player " + str(board.player) + ": ")
            coo_y = input("y coo for the player " + str(board.player) + ": ")
            valid_move = board.play_a_move((coo_x, coo_y))

            while valid_move == False:
                print("The coordinates you have provided are invalid. Please try again.")
                coo_x = input("x coo for the player " + str(board.player) + ": ")
                coo_y = input("y coo for the player " + str(board.player) + ": ")
                valid_move = board.play_a_move((coo_x, coo_y))

            board.compute_winner()

            if  board.winner != 0 or board.grid.all() == True: 
                end = True

            board.terminal_display()

        if  board.winner != 0: 
            print("The winner is the player " + str(board.winner))
        else: 
            print("Draw")

    else: 
        print("1 or 2")