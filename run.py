from random import randint
import time

# computer and player scores set to 0 
scores = {"computer":0, "player":0}
# Global variables for grid
player_grid_rows = 5
player_grid_column = 5
cpu_grid_rows = 5
cpu_grid_column = 5
#global name variable 
name = ()

class Player_Input:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores


    def get_player_name(self):
        self.name = input("Enter Name Here")
        print(f"Output:Welcome to the battle {self.name}")
        
        return self.name
    
    def check_player_name(self):
        if():
            name == ""
            print("please Enter Name")
        else:
            return self.name



   

   # def __init__(self.name)
    #    name = player_name


print("test1")
class grid_drawing():
    """
    this class draws out the grid
    """
    for i in range(player_grid_rows):
        
        for j in range(player_grid_column):
            
            print("O ", end="")
        
        print()
    print("__________ ")
    for i in range(player_grid_rows):
        
        for j in range(player_grid_column):
            
            print("O ", end="")
        
        print()


#class computer_choice():
    #"""
   # random number choice for the grid 
   # """
#class Ships():
    #def __init__(self)
#class Player():
#class User_input():
#class End_game