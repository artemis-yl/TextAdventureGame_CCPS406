import json
from classes import *



def import_items(item_filename):


    with open(item_filename,'r') as item_json:
        data=json.load(item_json)




    item_list=[]

    for item_key,item_data in data.items():
        name=item_data['name']
        description=item_data['description']
        item_type=item_data['type']
        new_item=None


        if item_type.lower()=='item':
            new_item=Item(name,description)
        
        elif item_type.lower()=='key':
            new_item=Key(name,description)

        elif item_type.lower()=='end':
            new_item=Ending_Item(name,description)

        elif item_type.lower()=='gift':
            use_error=item_data['use_error']
            new_item=Gift(name,description,use_error)
        
        
        if new_item is not None:
            item_list.append(new_item)
        

    

    return item_list


def import_rooms(room_filename,items_list):


    with open(room_filename,'r') as room_json:
        data=json.load(room_json)


    room_list=[]
    start_check=None

    for room_key,room_data in data.items():
        name=room_data['name']
        description=room_data['description']
        short_description=room_data['description2']
        inventory=room_data['inventory']
        hint=room_data['hint']

        

        new_room=Room(name,description,hint=hint,short_description=short_description)

        for item in inventory:
            if item in items_list:
                new_room.add_item(item)


        if 'player_start' in room_data:
            start_check=new_room

        room_list.append(new_room)
        

    if start_check is None:
        starting_room=room_list[1]

    else:
        starting_room=start_check
        starting_room.ending_room=True
        starting_room.visited=True
    

    return room_list,starting_room



def import_doors(door_filename,rooms_list):

    if rooms_list==[]:
        print("Rooms list is empty.")
        return


    with open(door_filename,'r') as door_json:
        data=json.load(door_json)




    puzzle_list=[]


    for door_key,door_data in data.items():
        

            
            
        connect_rooms=door_data['rooms']
        if not connect_rooms[0] in rooms_list or not connect_rooms[1] in rooms_list:
            continue
        direction=door_data['direction'][0]
        room=rooms_list[rooms_list.index(connect_rooms[0])]
        new_puzzle='solved'

        


        is_puzzle=door_data['is_puzzle']

        if is_puzzle=="True":
            name=door_data['name']
            state_descriptions=door_data['state_descriptions']
            state=door_data['state']
            key_item=door_data['key_item']
            key_verb=door_data['key_verb']

            new_puzzle=Puzzle(name,state_descriptions,key_item,key_verb,state)
            puzzle_list.append(new_puzzle)


        room.add_door(rooms_list[rooms_list.index(connect_rooms[1])],direction,new_puzzle)


            






        
        

    

    return puzzle_list


def import_npcs(npc_filename,rooms_list,items_list):


    with open(npc_filename,'r') as npc_json:
        data=json.load(npc_json)




    npc_list=[]

    for npc_key,npc_data in data.items():
        name=npc_data['name']
        description=npc_data['description']
        npc_type=npc_data['type']
        dialogue=npc_data['dialogue']
        current_room=npc_data['current_room']

        

        new_npc=None

        

        if current_room not in rooms_list:
            continue

        for room in rooms_list:

            if room.name==current_room:
                current_room=room       

        
            


        if npc_type.lower()=='gnpc':

            gift=npc_data['gift']

            

            if gift not in items_list:
                continue

            
            new_npc=GNPC(name,description,current_room,dialogue,gift)
        
        
        
        if new_npc is not None:
            npc_list.append(new_npc)
        
        

    

    return npc_list



def import_gameMsg(gameMsg_filename):


    with open(gameMsg_filename,'r',encoding='utf-8') as gameMsg_json:
        data_dict=json.load(gameMsg_json)
        introduction = data_dict["introduction"]
        youDied = data_dict["youDied"]
        youWinMinimal = data_dict["youWinMinimal"]
        youWinBestEnding = data_dict["youWinBestEnding"]
        # print(introduction)

    return introduction,youWinBestEnding

