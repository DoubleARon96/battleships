from random import randint
import time

# computer and player scores set to 0 
scores = {"computer":0, "player":0}
# Global variables for grid
player_grid_rows = 5
player_grid_column = 10
cpu_grid_rows = 5
cpu_grid_column = 10
#global name variable 
name = ()

class Player_Input:
    def __init__(self, player_name, game_scores):
        self.player_name = player_name
        self.game_scores = game_scores


    def get_player_name(self):
        self.player_name = ""
        
        while not self.player_name:
            
            self.name = input("Enter Name Here").strip()

            if not self.player_name:
                print("Name Is Required")

    
        print(f"Output:Welcome to the battle {self.name}")
        
        return self.player_name
    
    def check_player_name(self):
        """
        checks players name
        """
        if not self.player_name:
            print("please Enter Name")
            self.get_player_name()
    

player_name = input("Enter your name: ") # get the player name from the user
game_scores = [] # create an empty list for the game scores
player = Player_Input(player_name, game_scores) # create an instance of the class
player.check_player_name() # check the player name


player_name = Player_Input
print(player_name)

   # def __init__(self.name)
    #    name = player_name


print("test1")
class grid_drawing():
    def __init__(self, grid, ships, hits, misses,):
        """
        this class draws out the grid
        """
        self.grid = grid
        self.ships = ships
        self.hits = hits
        self.misses = misses

    def print_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j],end=" ")
            print()
    print("-------------------")

grid = [["O" for _ in range(10)] for _ in range(5)]
ships = [(0, 0), (1, 1), (4, 2)]
hits = [(0, 0), (1, 1)]
misses = [(3, 3), (4, 4)]

gd = grid_drawing(grid, ships, hits, misses)

# update the grid with the ships, hits, and misses
for i, j in ships:
    gd.grid[i][j] = "S"
for i, j in hits:
    gd.grid[i][j] = "H"
for i, j in misses:
    gd.grid[i][j] = "M"

gd.print_grid()


    #for i in range(cpu_grid_rows):
        
        #for j in range(cpu_grid_column):
            
            #print("O ", end="")
        
        #print()


#class computer_choice():
    #"""
   # random number choice for the grid 
   # """
#class Ships():
    #def __init__(self)
#class Player():
#class User_input():
#class End_game