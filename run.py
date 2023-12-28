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
    
    def get_player_choice(self):
        valid_input = False
        while not valid_input:
            print("Input Guild:first number is Y axis (0 To 4) and second number is X axis (0 To 9")
            player_input = input("Enter your choice: ")
            try:
                player_choice = list(map(int, player_input.split(",")))
                if(len(player_choice) != 2 ):
                    raise Exception("To Many Inputs")
                valid_input = True
            except Exception as e: 
                print(e)
                valid_input = False
        
        return player_choice





    

player = Player_Input()

player.check_player_name()

print(player.player_name)

class Battleship():
    #global variables
    # coords = {
    #     "X" : 0,
    #     "Y" : 0
    # }

    # Is_Alive = True

    '''
    This class is to check the grid if the player input is a miss or hit.
    '''
    def __init__(self, coords_X, coords_Y):
        self.coords_X = coords_X
        self.coords_Y = coords_Y
        self.Is_Alive = True

    def set_random_location(self):
        random_nums_Y = [0, 1, 2, 3, 4]
        random_num_choice_Y = random.choice(random_nums_Y)
        random_nums_X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random_num_choice_X = random.choice(random_nums_X)
        self.coords_X = random_num_choice_X
        self.coords_Y = random_num_choice_Y

    def check_hit_or_miss(self, X, Y):
        print(self.coords_X, self.coords_Y)
        if (X == self.coords_X and Y == self.coords_Y):
            self.Is_Alive = False
            return "Hit!"

        else:
            return "Miss!"


print("test1")
class grid_drawing():
    grid = [[],[]]
    
    """
    this class draws out the grid and updates the ships, hits, misses
    """
    def __init__(self, ships, misses):
        y = 5
        x = 10
        self.grid = [["O" for _ in range(x)] for _ in range(y)]

        # update the grid with the ships, hits, and misses
        self.grid[0][0] = "q"
        self.grid[0][9] = "w"
        self.grid[4][0] = "a"
        self.grid[4][9] = "s"
        for ship in ships:
            print(ship.coords_X, ship.coords_Y)
            if(ship.Is_Alive):
                self.grid[ship.coords_Y][ship.coords_X] = "S"
            else:
                self.grid[ship.coords_Y][ship.coords_X] = "H"
        # for i, j in hits:
        #     self.grid[i][j] = "H"
        for i, j in misses:
            self.grid[i][j] = "M"
        self.ships = ships
        self.hits = hits
        self.misses = misses

    def update_grid(self, ships, misses):
        for ship in ships:
            print(ship.coords_X, ship.coords_Y)
            if(ship.Is_Alive):
                self.grid[ship.coords_Y][ship.coords_X] = "S"
            else:
                self.grid[ship.coords_Y][ship.coords_X] = "H"
        for i, j in misses:
            self.grid[i][j] = "M"

    def print_grid(self):
        print("----------------------")
        print("|      0123456789    |")
        for i in range(len(self.grid)):
            print("|    " + str(i) + " ",end="")
            for j in range(len(self.grid[i])):
                # This code will hide the ships and empty spaces
                # So you can easily hide the grid
                if(self.grid[i][j] == "S" or self.grid[i][j] == "O"):
                    print("?", end="")
                else:
                    print(self.grid[i][j],end="")
            print("    |")
        print("----------------------")
    #these help choose where the ships spawn on the grid
random_nums_Y = [0, 1, 2, 3, 4]
random_num_choice_Y = random.choice(random_nums_Y)
random_nums_X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random_num_choice_X = random.choice(random_nums_X)
ship1 = Battleship(random_num_choice_X, random_num_choice_Y)

ship2 = Battleship(0,0)
ship2.set_random_location()

ship3 = Battleship(0,0)
ship3.set_random_location()
print("Ship1: " + str(ship1.coords_X) + ", " + str(ship1.coords_Y))
print("Ship2: " + str(ship2.coords_X) + ", " + str(ship2.coords_Y))
print("Ship3: " + str(ship3.coords_X) + ", " + str(ship3.coords_Y))
grid = [["O" for _ in range(10)] for _ in range(5)]

ships = [ship1, ship2, ship3]
hits = [(4, 9), (1, 1)]
misses = []

gd = grid_drawing(ships, misses)



gd.print_grid()
'\n'
player_choice = player.get_player_choice()
print(player_choice)

num_misses = 0
for ship in ships:
    result = ship.check_hit_or_miss(player_choice[0], player_choice[1])
    if(result == "Miss!"):
        num_misses += 1
    else:
        print(result)

if(num_misses == len(ships)):
    misses.append((player_choice[0], player_choice[1]))

gd.update_grid(ships, misses)
gd.print_grid()

# input_checker = Player_Input_checks(game.player_choice, game.misses, game.hits)


class Player_Input_checks():

    
    def __init__(self, player_choice, misses, hits):
        
        self.player_choice = player_choice
        self.misses = misses
        self.hits = hits

    
    def check_input(self, input):
        if len(input) == 2:
            if input[0].isalpha() and input[0].upper() in "ABCDE":
                if input[1].isnumeric() and int(input[1]) in range(0, 11):
                    if input in ships:
                        return True

        return False
    
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
class End_game:
    def __init__(self, lives, score, rounds):
        self.lives = lives
        self.score = score
        self.rounds = rounds
    
    def count_rounds(self):
        for round in range (1, self.rounds +1):

             print(f"Round {round} of {rounds}")
             game_over = False

        if game_over:
            print("Game Over")