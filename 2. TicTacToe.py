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
    def __init__(self):
        self.player_token = "0"
        self.row_guide = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]
        self.board_guide = np.array(self.row_guide)
        self.dictionary_values = {
            "A1": [0, 0], "A2": [0, 1], "A3": [0, 2],
            "B1": [1, 0], "B2": [1, 1], "B3": [1, 2],
            "C1": [2, 0], "C2": [2, 1], "C3": [2, 2],
        }

    def condition(self, coord, board_array):
        """Returns array where the contents are currently not filled with a player token"""
        return board_array[coord[0], coord[1]] == "_"

    def choose_move(self, board_current_state):
        """Returns an update board if the board isn't full"""
        # List comprehension which iterates through dictionary_values and keeps only the indices
        # where our condition is met (i.e. no player-token).
        valid_indices = [index for index, coord in self.dictionary_values.items()
                         if self.condition(coord, board_array=board_current_state.board_array)]
        # If there is a blank field
        if valid_indices:
            # Makes a random choice of these indices
            random_field_choice = np.random.choice(valid_indices)
            # We then look up the coordinates using our dictionary
            coordinates = self.dictionary_values[random_field_choice]
            # TESTING CODE PRINTING
            print(f"Randomly chosen field: {random_field_choice}")
            print(f"Corresponding coordinates: {coordinates}")
            # Update the board with that token using our coordinates
            board_current_state.board_array[coordinates[0], coordinates[1]] = "0"
            # Return the updated board
            return board_current_state
        else:
            print("No valid choices.")
            return board_current_state  # Return the original board


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
        """Returns the player's choice if a valid move or returns False otherwise"""
        # Print out current board
        self.print_current_board()
        user_choice = input("\nPlace your move using the codes shown above.")
        #  If the user choice is in the dictionary its valid
        if user_choice in self.dictionary_values:
            # Grab our indices from the dictionary_values
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
        print(f"PLayer token is {self.player_token}")
        """Returns True if there is a win otherwise returns False"""
        if any(np.all(board.board_array == self.player_token, axis=1)):
            print("Horizontal/row win")
            self.show_winner_details(board=board)
            return True
        elif any(np.all(board.board_array == self.player_token, axis=0)):
            print("Vertical/col win")
            self.show_winner_details(board=board)
            return True
        elif board.board_array[0][0] == self.player_token \
                and board.board_array[1][1] == self.player_token \
                and board.board_array[2][2] == self.player_token:
            print("Diagonal Win")
            self.show_winner_details(board=board)
            return True
        elif board.board_array[0][2] == self.player_token \
                and board.board_array[1][1] == self.player_token \
                and board.board_array[2][0] == self.player_token:
            print("Diagonal Win")
            self.show_winner_details(board=board)
            return True
        else:
            print("No win")
            print(board.board_array)
            return False

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_winner_details(self, board):
        # Clearing the Screen
        # self.clear_screen()
        print(logo)
        board.print_current_board()


def choose_game_type():
    game_choice = False
    while game_choice == False:
        # Ask for how many players
        game_choice = input(
            "Would you like to play against the computer (press 1)\nor against another player? (press 2)")
    # 2 Player game logic
    if game_choice == '2':
        return 2
    elif game_choice == '1':
        return 1


def run_game():
    # Create board instance
    board = Board()
    game_instance = GameManagement()
    game_chosen = choose_game_type()
    if game_chosen == 2:
        # ------------------------ GAME LOGIC FOR TWO PLAYERS ----------------------- >>
        while not game_instance.game_over:
            # Clearing the Screen
            # game_instance.clear_screen()
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

    elif game_chosen == 1:

        # ------------------------ GAME LOGIC FOR ONE PLAYER VS AI  ----------------------- >>
        print("AI TIME")
        ai = AI()
        while not game_instance.game_over:
            # Clearing the Screen
            # game_instance.clear_screen()
            board.print_guide()
            print(f"\nCurrent player is: {game_instance.current_player}")
            if game_instance.current_player == "Player_1":
                board.make_move_on_board(player_token=game_instance.player_token)

                if game_instance.check_for_win(board=board):
                    game_instance.game_over = True
                    print(f"\n{game_instance.current_player} wins!")

                game_instance.change_turn()
            # AI IS ALWAYS PLAYER 2
            elif game_instance.current_player == "Player_2":
                print(f"AI player token is: {ai.player_token}")  # TEST CODE
                # Check for Win
                if game_instance.check_for_win(board=board):
                    game_instance.game_over = True
                    print(f"\n{game_instance.current_player} wins!")
                # Check for Game_over
                game_instance.check_for_game_over(board=board)
                # Make move and update board
                board = ai.choose_move(board_current_state=board)
                # Change the turn
                game_instance.change_turn()


if __name__ == '__main__':
    run_game()
