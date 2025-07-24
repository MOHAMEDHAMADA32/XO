import os

# Clear the terminal screen
# Note: On Linux/Mac use "clear" instead of "cls"
def clear_screen():
    os.system("cls")

# -----------------------------
# Player class manages user name and symbol
# -----------------------------
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    # Get a valid name from the user
    def choose_name(self):
        while True:
            name = input("Pls enter your name(letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Pls use letters only")

    # Get a valid symbol (1 character, alphabet)
    def choose_symbol(self):
        while True:
            symbol = input(f"Hi {self.name} choose your symbol (a single letter only): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Pls choose a valid one")

# -----------------------------
# Menu class handles main and endgame menus
# -----------------------------
class Menu:
    # Display the start menu
    def display_main_menu(self):
        main_menu_text = """
        Welcome to my X-O game!
        1. Start Game
        2. Quit Game
        Enter your choice (1 or 2): """

        while True:
            choice = input(main_menu_text)
            value = self.validate(choice)
            if value == 'valid':
                return choice
            elif value == 'invalid':
                print('Invalid value. Select between (1 or 2)')

    # Display the endgame (restart or quit)
    def display_endgame_menu(self):
        endgame_menu_text = """
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2): """

        while True:
            choice = input(endgame_menu_text)
            value = self.validate(choice)
            if value == 'valid':
                return choice
            elif value == 'invalid':
                print('Invalid value. Select between (1 or 2)')

    # Validate menu input
    def validate(self, choice):
        choice_values = [1, 2]
        try:
            choice = int(choice)
            if choice in choice_values:
                return "valid"
        except ValueError:
            return "invalid"

# -----------------------------
# Board class manages the state of the game board
# -----------------------------
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    # Print the board to the console
    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 5)

    # Update a cell with the player's symbol
    def update_board(self, index, symbol):
        if self.is_valid_move(index):
            self.board[index - 1] = symbol
            clear_screen()
            return True
        else:
            return False

    # Check if a move is valid (cell is not taken)
    def is_valid_move(self, index):
        return self.board[index - 1].isdigit()

    # Reset the board to its initial state
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

# -----------------------------
# Game class ties everything together and controls the game flow
# -----------------------------
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    # Start the game by showing menu and initializing players
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    # Setup players' names and symbols
    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, Enter your details:")
            player.choose_name()
            while True:
                player.choose_symbol()
                if number == 2 and player.symbol == self.players[0].symbol:
                    print("This symbol is already taken by Player 1. Please choose another one.")
                else:
                    break
            clear_screen()

    # Main game loop that handles turns and checks win/draw
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_drow():
                self.winner_player()
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    # Determine and display the winner (or draw)
    def winner_player(self):
        if self.check_win():
            winner = self.players[self.current_player_index - 1].name
            print(f"The winner player is: {winner}")
            self.board.display_board()
        elif self.check_drow():
            print("No winner, it's a draw.")
        else:
            return

    # Reset game state to play again
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    # Check for win conditions
    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]
        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    # Check if the board is full with no winner
    def check_drow(self):
        return all(not cell.isdigit() for cell in self.board.board)

    # Handle a player's move
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol}):")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        self.switch_player()

    # Switch to the other player
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    # Exit the game
    def quit_game(self):
        print("Thank you for playing!")

# -----------------------------
# Start the game
# -----------------------------
play = Game()
play.start_game()
