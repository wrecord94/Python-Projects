import numpy as np
import os

logo = ''' 
 _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ |
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|
                                        '''

# FUTURE IMPROVEMENTS
# -> AI to play against!
class AI:
    pass


class Board:

    def __init__(self):
        self.row_list = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.row_guide = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]
        self.dictionary_values = {
            "A1": [0, 0], "A2": [0, 1], "A3": [0, 2],
            "B1": [1, 0], "B2": [1, 1], "B3": [1, 2],
            "C1": [2, 0], "C2": [2, 1], "C3": [2, 2],
        }
        self.board_array = np.array(self.row_list)
        self.board_guide = np.array(self.row_guide)

    def print_guide(self):
        """Prints the game guide."""
        print(logo)
        print("\nGUIDE \n")
        print(self.board_guide)

    def print_current_board(self):
        """Prints the current state of the game board."""
        print("\nCURRENT BOARD\n")
        print(self.board_array)

    def make_move_on_board(self, player_token):
        # Print out current board
        self.print_current_board()
        user_choice = input("\nPlace your move using the codes shown above.")

        if user_choice in self.dictionary_values:
            indices = self.dictionary_values[user_choice]
            if self.board_array[indices[0], indices[1]] == "_":
                self.board_array[indices[0], indices[1]] = player_token
                return user_choice
            else:
                print("Invalid move. The space is already taken. Choose a different space.")
                return False
        else:
            print("Invalid move code. Please choose a valid code.")
            return False

    def check_for_full(self):
        """Returns True if the board is full"""
        if "_" in self.board_array:
            # print("Not Full")
            return False
        else:
            # print("Full")
            return True


class GameManagement:

    def __init__(self):
        self.players = ["Player_1", "Player_2"]
        self.current_player = self.players[0]
        self.game_over = False
        self.player_token = "X"
        # self.player_tokens = {"Player_1": "X",
        #                       "Player_2": "0"}

    def change_turn(self):
        # print(f"Current player is: {self.current_player}")
        # Change the player
        if self.current_player == "Player_1":
            self.current_player = "Player_2"
            # Change token
            self.player_token = "0"
        else:
            self.current_player = "Player_1"
            self.player_token = "X"
        #     We return the user's choice
        return True

    def check_for_game_over(self, board):
        if board.check_for_full():
            self.game_over = True
        else:
            pass

    def check_for_win(self, board):
        """Returns True if there is a win otherwise returns False"""
        if any(np.all(board.board_array == self.player_token, axis=1)):
            # print("Horizontal/row win")
            self.show_winner_details(board=board)
            return True
        elif any(np.all(board.board_array == self.player_token, axis=0)):
            # print("Vertical/col win")
            self.show_winner_details(board=board)
            return True
        elif board.board_array[0][0] == self.player_token \
                and board.board_array[1][1] == self.player_token \
                and board.board_array[2][2] == self.player_token:
            # print("Diagonal Win")
            self.show_winner_details(board=board)
            return True
        elif board.board_array[0][2] == self.player_token \
                and board.board_array[1][1] == self.player_token \
                and board.board_array[2][0] == self.player_token:
            # print("Diagonal Win")
            self.show_winner_details(board=board)
            return True
        else:
            # print("No win")
            return False

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def show_winner_details(self, board):
        # Clearing the Screen
        self.clear_screen()
        print(logo)
        board.print_current_board()


def run_game():
    # Create board instance
    board = Board()
    game_instance = GameManagement()

    while not game_instance.game_over:
        # Clearing the Screen
        game_instance.clear_screen()
        board.print_guide()
        print(f"\nCurrent player is: {game_instance.current_player}")
        while not board.make_move_on_board(player_token=game_instance.player_token):
            # Prompt the player to make a valid move
            print("Invalid move. Please choose a different space.")
        # Check for Win
        if game_instance.check_for_win(board=board):
            game_instance.game_over = True
            print(f"\n{game_instance.current_player} wins!")

        # Check for Game_over
        game_instance.check_for_game_over(board=board)

        # Change the turn
        game_instance.change_turn()


if __name__ == '__main__':
    run_game()
