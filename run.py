from random import randint
import time
import random

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
    def __init__(self, player_name=None,):
        if not player_name:
            player_name = self.get_player_name()


            
        self.player_name = player_name


    def get_player_name(self):
        player_name = ""
        
        while not player_name:
            
            player_name = input("Enter Name Here ").strip()

            if not player_name:

                print("Name Is Required")

    
        print(f"Output:Welcome to the battle {player_name}")
        
        self.player_name = player_name
        return self.player_name
    
    def check_player_name(self):
        """
        checks players name
        """
        if not self.player_name:
            print("please Enter Name")
            self.player_name = self.get_player_name()
    
    

player = Player_Input()

player.check_player_name()

print(player.player_name)


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
    #these help choose where the ships spawn on the grid
random_nums = [0, 1, 2, 3, 4]
random_num_choice = random.choice(random_nums)
random_nums_X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random_num_choice_X = random.choice(random_nums_X)
grid = [["O" for _ in range(10)] for _ in range(5)]
ships = [(random_num_choice, random_num_choice_X), (random_num_choice, random_num_choice_X), (random_num_choice, random_num_choice_X)]
hits = [(4, 9), (1, 1)]
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
'\n'
print("Input Guild:first number is Y axis (0 To 4) and second number is X axis (0 To 9")
    


class Battleship():
    '''
    This class is to check the grid if the player input is a miss or hit
    '''
    def __init__(self,player_choice, misses, hits):

        self.player_choice = player_choice
        self.misses = misses
        self.hits = hits
        
        player_choice = input()

    def check_hit_or_miss(x, y):
    
        if (x, y) in ships:
            return "Hit!"
    
        elif (x, y) in misses:
            return "Miss!"
    
        else:
            return "Empty!"
    
game = Battleship(input("Enter your choice: "),[],[])

input_checker = Player_Input_checks(game.player_choice, game.misses, game.hits)

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
#class End_game:
    #def __init__(self, lives, score, rounds):
       # self.lives = lives
        #self.score = score
       # self.rounds = rounds
    
    #def count_rounds(self):
        #while