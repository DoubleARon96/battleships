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
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores


    def get_player_name(self):
        self.name = ""
        
        while not self.name:
            
            self.name = input("Enter Name Here")

            if not self.name:
                print("Name Is Required")

    
        print(f"Output:Welcome to the battle {self.name}")
        
        return self.name
    
    def check_player_name(self):
        if():
            self.name == ""
            print("please Enter Name")
        else:
            return self.name



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
ships = [(0, 0), (1, 1), (2, 2)]
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