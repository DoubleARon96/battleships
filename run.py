import random
import time

# computer and player scores set to 0 
scores = {"computer":0, "player":0}


# Global variables for grid
grid = [[]]

grid_size = 10

num_of_ships = 8

bullets_left = 50

game_over = False

num_of_ships_sunk = 0

ship_positions = [[]]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Playground:
    """
    the main playground class set and sizes set also sets the amount of ships per playground 
    and sets out the playground
    """

    def grid (start_row, end_row, start_col, end_col):
        global grid
        global ship_positions

        all_safe = True
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                if grid [r][c] != ".":
                    all_safe = False
                    break
                if not all_safe:
                    break


        if all_safe:
            ship_positions.append([start_row, end_row, start_col, end_col])
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    grid[r][c] ="X"

        return all_safe



#class Newgame:
   # def __init__()