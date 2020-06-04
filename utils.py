import subprocess
# Helper functions

def is_finished(the_map, input_x, input_y):
    if the_map[(input_x, input_y)] == "X":
        print("You are finished, congratz - The reward was a joke. LOLz")
        exit()
    
def allowed_step(the_map, input_x, input_y):
    # Check if it is a valid input
    if the_map[(input_x, input_y)] != "*":
        return True
    return False

def traverse_tree(direction, the_map, current_x, current_y, new_pos_x, new_pos_y):
    
    subprocess.run("clear")
    # Check if we are done
    is_finished(the_map, new_pos_x, new_pos_y)
    
    print(f"You chose: {direction}")

    # Check if it is an allowed step
    if allowed_step(the_map, new_pos_x, new_pos_y):
        print("That was a valid move")
        current_x, current_y = new_pos_x, new_pos_y
        return current_x, current_y
    
    # If it was not a valid move or we did not find the end, we let the user try again
    print("Invalid move.. Please try again")
    return current_x, current_y


def print_state():
    temp_list = list(local_dict.values())

    chunks = [temp_list[x:x+20] for x in range(0, len(temp_list), 20)]
    for chunk in chunks:
        print("".join(chunk)+"\n")

    
def set_current_state(POS_X, POS_Y):
    # Visited Nodes
    local_dict[(POS_X, POS_Y)] = "*"

def get_state(POS_X, POS_Y):
    local_dict[(POS_X, POS_Y)] = "X"

def handle_move(the_map, direction, POS_X, POS_Y):
    
    set_current_state(POS_X, POS_Y)

    if direction == "up":
       POS_X, POS_Y = traverse_tree(direction, the_map, POS_X,POS_Y,POS_X-1,POS_Y)
    elif direction == "down":
       POS_X, POS_Y = traverse_tree(direction, the_map, POS_X,POS_Y,POS_X+1,POS_Y)
    elif direction == "left":
       POS_X, POS_Y = traverse_tree(direction, the_map, POS_X,POS_Y,POS_X,POS_Y-1)
    elif direction == "right":
       POS_X, POS_Y = traverse_tree(direction, the_map, POS_X,POS_Y,POS_X,POS_Y+1)

    get_state(POS_X, POS_Y)
    print_state()
    return POS_X,POS_Y


local_dict = {}

def intialize_game(the_map):
    global local_dict
    local_dict = the_map.copy()
    for ele in local_dict:
        local_dict[ele] = " "