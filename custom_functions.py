from main_imports import *

def move(current_room,rooms_list,direction="N"):

    

    if direction.upper() not in ["N","E","W","S"]:
        print("Invalid Direction")
        return current_room

    direction_index=["N","E","W","S"].index(direction.upper())

    

    door=current_room.connected_doors[direction_index]

   

    

    if isinstance(door,Puzzle):
        door = door.state

    if door=="solved":
        return current_room.connected_rooms[direction_index]

    elif door=="NULL":
        print("No door present.")
    
    elif door=="unsolved":
        print("Path blocked.")
    
    
    
    
    
    return current_room



def create_action_dictionary(game_state):

    action_dic={}
    action_dic['move']=['North','East','West','South','N','E','W','S']
    current_room=game_state.current_room
    action_dic['use']=game_state.inventory
    action_dic['take']=current_room.inventory
    action_dic['discard']=game_state.inventory
    action_dic['scan'] = ['scan'] 
    action_dic['inventory'] = ['inventory']
    action_dic['give'] = game_state.inventory
    action_dic['hint'] = ['hint']

    return action_dic

def parse_input(user_input, current_game_state):

    max_input_length=80

    if user_input=="":
        print("Invalid input.")
        return "invalid","invalid"
    
    
    

    
    if len(user_input)>max_input_length:
        print('Input too long. Inputs should be under 80 characters.')
        return "invalid","invalid"
    
    action_dic={}
    action_dic=create_action_dictionary(current_game_state)


    input_list=user_input.split()

    if len(input_list)<1:
        print("Invalid input.")
        return "invalid","invalid"

    if input_list[0].lower()=='say' and len(input_list)>1:

        response=user_input[4:].capitalize()
        return "say",response

    pairs_made=0
    verb_used=""
    command_used=""
    command_list=[]
    for word in input_list:
        if word.lower() in action_dic:
            verb_used=word.lower()
            command_list=action_dic[verb_used]

            for command_word in input_list:
                if command_word.lower() in (command_list_word.lower() for command_list_word in command_list):
                    # print(command_word)
                    command_used=command_word
                    pairs_made+=1


    if pairs_made!=1:
        print("Invalid input.")

        return "invalid","invalid"
    else:
        return verb_used,command_used



def item_use_fail():
        print('Nothing happens.')


def find_item(item_name,items_list):

    for item in items_list:
        if item.name.lower()==item_name.lower():
            return item
        
    return None

def find_room(room_name,rooms_list):

    for room in rooms_list:
        if room_name==room:
            return room
    
    return None

def find_puzzle(puzzle_name,puzzles_list):
    
    for puzzle in puzzles_list:
        if puzzle_name==puzzle:
            return puzzle
        
    return None




def unlock_all_doors(rooms_list):

    for room in rooms_list:

        doors=room.connected_doors

        for i in range(len(doors)):
            if doors[i]=="NULL":
                continue

            else:
                doors[i]='solved'





