from get_map import create_map
from utils import handle_move, intialize_game
from board_gen import main as bg

#POS_X, POS_Y = 1,1

#my_map = create_map("board.txt")

my_map, POS_X, POS_Y = bg((15, 15))


print("Welcome to the game")
print("Reach the end of the maze - and be rewarded!")

intialize_game(my_map)

#print(my_map, POS_X, POS_Y)

while True:
    direction = str(input("Choose a direction ")).lower()
    POS_X, POS_Y = handle_move(my_map, direction, POS_X, POS_Y)
