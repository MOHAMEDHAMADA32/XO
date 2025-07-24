import os
def clear_screen():
    os.system("cls")

class Player:
    def __init__(self):
        self.name=""
        self.symbol =""
    def choose_name(self):
        while True:
            name=input("Pls enter your name(letteers only): ")
            if name.isalpha():
                self.name=name
                break
            print("Invalid name .Pls use letters only")

    def choose_symbol(self):
        while True :
            symbol=input(f"Hi {self.name} choose your symbol (a singel letter only): ")
            if symbol.isalpha() and len(symbol)==1:
                self.symbol=symbol.upper()
                break
            print("Invalid symbol. Pls choose a valid one")



class Menu:
   
    def display_main_menu(self):
        main_menu_text="""
        welcome to my X-O game!
        1.Start Game
        2.Quit Game
        Enter your choice (1 or 2)"""

        while True:
            choice = input(main_menu_text)
            value=self.validate(choice)
            if value=='valid':
                return choice
                break
            elif value=='invalid':
                print('Invalid value. Select between (1 or 2)')
                
                
                
            
    def display_endgame_menu(self):
        
        endgame_menu_text ="""
        Game Over!
        1.Restart Game
        2.Quit Game
        Enter your choice (1 or 2)"""
        
        while True:
            choice=input(endgame_menu_text)
            value= self.validate(choice)
            if value=='valid':
                return choice
                break
            elif value=='invalid':
                print('Invalid value. Select between (1 or 2)')           
          
    


    def validate(self,choice):
        choice_values=[1,2]
        try:
            choice=int(choice)
            if choice in choice_values:
                return "valid"
        except ValueError:
            return "invalid"
        

class Board:
    def __init__(self):
         self.board=[str(i) for i in range(1,10) ]

    def display_board(self):
        for i in range (0,10,3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)

    def update_board(self,index,sympol):
        if self.is_valid_move(index) :
           self.board[index-1]= sympol
           clear_screen()
           return True
        else:
            return False
    
    def is_valid_move(self,index):
        return self.board[index-1].isdigit()
        
        
    def reset_board(self):
        self.board=[str(i) for i in range(1,10) ]


class Game:
    def __init__(self):
        self.players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
        self.current_player_index=0
    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice =="1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    def setup_players(self):
        for numper ,player in enumerate(self.players, start=1):
            print(f"Player {numper} , Enter your details: ")
            player.choose_name()
            while True:
                player.choose_symbol()
                if numper==2 and player.symbol==self.players[0].symbol:
                    print("This Symbol is already taken py player 1 . Plaese choose another noe")
                else:
                    break
                clear_screen()

    def play_game (Self):

        while True:
          Self.play_turn()
          if Self.check_win() or Self.check_drow():
                Self.winner_player()
                choice=Self.menu.display_endgame_menu()
                
                if choice=="1":
                    Self.restart_game()
                else:
                    Self.quit_game()
                    break
                  
    
    def winner_player(self):
        if self.check_win():
            winner=self.players[self.current_player_index-1].name
            print(f"The winner player is :{winner} ")
            self.board.display_board()
        elif self.check_drow():
            print("No winner it is a drow")
        else:
            return

    def restart_game(self):

        self.board.reset_board()
        self.current_player_index=0
        self.play_game()

    def check_win(self):
        
        win_combinations =[
            [0,1,2],[3,4,5],[6,7,8],##rows
            [0,3,6],[1,4,7],[2,5,8],#columns
            [0,4,8],[2,4,6] ## diagonals
        ]

        for combo in win_combinations:
            if (self.board.board[combo[0]]) == (self.board.board[combo[1]])==(self.board.board[combo[2]]):
                return True
        return False

    def check_drow(self):

       return all(not cell.isdigit()  for cell in self.board.board)


    def play_turn(self):

        player=self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol}: ) ")
        while True:
            try:
                cell_choice=int(input("choose a cell (1-9)"))
                if  1<= cell_choice <=9 and self.board.update_board(cell_choice,player.symbol):
                    break
                else :
                    print("Invalid move , try again")
            except ValueError:
                print("Pls Enter a value between (1 and 9): ")
        self.switch_player()

    def switch_player(self):
        self.current_player_index =1 - self.current_player_index

    def quit_game(self):

        print("Thank you for playing !")

play=Game()
play.start_game()