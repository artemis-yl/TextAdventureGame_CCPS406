import random

class Container:
    def __init__(self, name, description):
        self.name=name
        self.description=description

    def __eq__(self,other):

        if isinstance(other,Container):

            return ((self.name.lower()==other.name.lower()) and type(self)==type(other))
        
        else:
            return self.name.lower()==other.lower()



    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    









class Room(Container):
    def __init__(self, room_name, description,hint="",short_description=""):
        super().__init__(room_name,description)
        self.inventory=[]

        self.visited=False
        self.short_description=short_description

        #[N, E, W, S]
        self.connected_rooms=['NULL','NULL','NULL','NULL']
        self.connected_doors=['NULL','NULL','NULL','NULL']
        self.puzzles=[]
        self.hint=hint


        #Ending stuff
        self.ending_room=False

    

    def add_door(self,other,direction,door='solved'):

        if not isinstance(other,Room) or not direction in ['N','E','W','S'] or other==self:
            print("Invalid input.")
            return
        

        
        add_loc=['N','E','W','S'].index(direction)

        if not self.check_available_door(other,add_loc):
            print('Cannot add door.')
            return

        self.connected_rooms[add_loc]=other
        self.connected_doors[add_loc]=door

        #len(connected_rooms) is 3
        other.connected_rooms[3-add_loc]=self
        other.connected_doors[3-add_loc]=door
        return

    

    def add_item(self,added_item):
        if added_item not in self.inventory and isinstance(added_item,Item):
            self.inventory.append(added_item.name)

        elif added_item not in self.inventory:
            self.inventory.append(added_item)
        
        return

    
    def remove_item(self,removed_item):
        if removed_item in self.inventory and isinstance(removed_item,Item):
            self.inventory.remove(removed_item.name)
        elif removed_item in self.inventory:
            self.inventory.remove(removed_item)

        return
    


    def check_available_door(self,other,add_loc):

        if other.name in self.connected_rooms:
            return False
        
        elif self.connected_rooms[add_loc]!='NULL' or other.connected_rooms[3-add_loc]!='NULL':
            return False

        else:
            return True
        

    def get_connected_rooms(self):
        return self.connected_rooms
    
    def get_connected_doors(self):
        return self.connected_doors
    

    def get_door_puzzles(self):

        puzzle_list=[]

        for i in self.connected_doors:

            if i!='NULL' and i!='solved':
                puzzle_list.append(i)

        return puzzle_list
    

    def get_room_description(self):
        
        if self.visited:
            room_descr=self.short_description

        else:
            room_descr=self.description
            self.visited=True
        

        final_description=room_descr
        #+'\n'+doors_description+'\n'+item_description


        return final_description
    
    def get_scan_description(self):
        door_counter=0
        door_locs=['north','east','west','south']
        door_locations=""
        for i in range(len(self.connected_doors)):
            if self.connected_doors[i]!="NULL":
                door_counter+=1
                door_locations=door_locations+"One to the "+door_locs[i]+'. '
        
        doors_description="There are "+str(door_counter)+" door(s) in the room. "+door_locations

        item_counter=0
        
        items=self.get_room_inventory()

        if items is None:
            item_description="There are no items inside the room."
        
        else:
            item_description="There are "+str(len(items))+" item(s) inside the room"
            item_description=item_description+': '

            for i in items:
                item_description=item_description+'A '+str(i)+'. '
        
        final_scan_description = doors_description+'\n'+item_description

        return final_scan_description
    
    def get_hint(self):
          return self.hint

    def get_room_inventory(self):

        if not self.inventory:
            return None
        
        else:
            return self.inventory
    

    def unlock_door(self,door_name):


        if door_name in self.connected_doors:
            door_index=self.connected_doors.index(door_name)

            second_room=self.connected_rooms[door_index]

            self.connected_doors[door_index]='solved'
            second_room.connected_doors[3-door_index]='solved'

        return

            

        
    








class Item(Container):

    def __init__(self, name, description):
        super().__init__(name,description)

        #purpose=[Key, Weapon, Shield, Teleporter, Revive]
        self.purpose=[False,False,False,False,False]
    

    def get_purpose(self):
        return self.purpose
    
    def give_item(self,current_game_state):

        print('That item is not giftable.')

        return

    def use_item(self,current_game_state):

        print("That item cannot be used.")
        return

    

class Key(Item):
    def __init__(self, name, description):
        super().__init__(name,description)
        self.purpose=[True, False,False,False,False]

    
    def use_item(self,current_game_state):

        current_room=current_game_state.current_room

        item_use_text="You used the "+self.name+'. '
        doors=current_room.get_door_puzzles()

        success=False

        if doors is not None:

            for door in doors:

                if door.key.lower()==self.name.lower():
                    item_use_text=item_use_text+'A door in the room unlocks.'
                    current_room.unlock_door(door.name)
                    success=True
        
        if not success:
            item_use_text=item_use_text+'It seems to have no effect.'
        
        print(item_use_text)
        return


class Ending_Item(Item):
    def __init__(self, name, description):
        super().__init__(name,description)
        self.purpose=[True, False,False,False,False]
        self.use_room=None

    
    def use_item(self,current_game_state):

        if self.use_room==None:
            current_game_state.start_ending()
            return
            

        if current_game_state.current_room==self.use_room:

            current_game_state.start_ending()

        return
    

    def set_use_room(self,room):
        self.use_room=room

    

class Gift(Item):
    def __init__(self, name, description,use_error):
        super().__init__(name,description)
        self.use_error=use_error
        self.purpose=[True, False,False,False,False]


    def use_item(self,current_game_state):

        print(self.use_error)

        return
    
    def give_item(self,current_game_state):

        current_room=current_game_state.current_room

        npcs_list=current_game_state.npcs_list

        if npcs_list==[]:
            print('No one in the room wants that item.\n')
            return
        
        else:

            for npc in npcs_list:
                if npc.current_room==current_room and type(npc)==GNPC:
                    if npc.gift.lower()==self.name.lower():
                        npc.gift_success(current_game_state)
                        return True



        return False










class Puzzle(Container):
    def __init__(self, name, state_descriptions,
                 key,key_verb,
                 state="unsolved"):
        super().__init__(name,state_descriptions[state])
        self.state_descriptions=state_descriptions
        self.state=state
        self.key=key
        self.key_verb=key_verb


    

    def update_state(self,new_state="unsolved"):
        if new_state=="solved" or new_state=="unsolved":
            self.state=new_state
            self.description=self.state_descriptions[new_state]


    

    def check_solution(self,verb_input,key_input):
        
        if self.key.lower()==key_input.lower() and self.key_verb.lower()==verb_input.lower():
            return True
        else:
            return False
        








class GameState:
    def __init__(self,current_room,rooms_list,items_list,npcs_list, player="Player"):
        self.player=player
        self.rooms_list=rooms_list
        self.items_list=items_list
        self.npcs_list=npcs_list
        self.inventory=[]
        self.current_room=current_room
        self.solved_puzzles=[]
        self.loop_condition=True

        #0 = Bad, 1=Good, 2=whatever (print at end)
        self.ending=1
        self.ending_sequence=False
        self.ending_counter=0



    
    def add_item(self,added_item):
        if added_item not in self.inventory and isinstance(added_item,Item):
            self.inventory.append(added_item.name)

        elif added_item not in self.inventory:
            self.inventory.append(added_item)
        
        return

    
    def remove_item(self,removed_item):
        if removed_item in self.inventory and isinstance(removed_item,Item):
            self.inventory.remove(removed_item.name)
        elif removed_item in self.inventory:
            self.inventory.remove(removed_item)

        return

    

    def add_puzzle(self,added_puzzle):
        if isinstance(added_puzzle,Puzzle):
            self.solved_puzzles.append(added_puzzle)

    

    def change_room(self,new_room):
        if isinstance(new_room,Room):
            self.current_room=new_room

            enter_room='You enter '+self.current_room.name+'.\n'
            room_description=self.current_room.get_room_description()


            txt_to_print=room_description
            print(txt_to_print)

    

    def start_ending(self):

        print('You carefully place the explosive, and initiate the countdown. You better escape to the hangar bay.')
        self.ending_sequence=True

    
    def add_ending_counter(self):


        if self.ending_sequence==True:
            self.ending_counter+=1

            if self.current_room.ending_room:
                self.loop_condition=False
                return

        if self.ending_counter==10:
            self.ending=0
            self.loop_condition=False
            return
            
        
        return





    

    def __str__(self):
        return f"""Current Game State
Player Name: {self.player}
Items: {self.inventory}
Current Room: {self.current_room}
Solved Puzzles: {self.solved_puzzles}"""
    
    def __repr__(self):
        return f"Player Name: {self.player}"
    
    




class NPC(Container):
    def __init__(self, npc_name, description,current_room,dialogues):
        super().__init__(npc_name,description)
        self.current_room=current_room
        self.dialogues=dialogues
        self.roaming=True
        self.first_meeting=True
        self.static=False


    
    def do_roam(self,current_game_state):

        rng=random.randint(0,3)
        

        connected_rooms=self.current_room.connected_rooms
        connected_rooms[rng]

        if connected_rooms[rng]!="NULL":
            self.current_room=connected_rooms[rng]
        
        return
    

    def roam(self,current_game_state):

        if current_game_state.current_room==self.current_room:

            self.interact()

        elif self.roaming:
            self.do_roam(current_game_state)

        else:
            return

            
    def interact(self):

        if self.first_meeting:

            interaction_dialogue="A Trooper Guard enters the room.\n"
            interaction_dialogue=interaction_dialogue+"\"Who are you? You're not supposed to be in here!\" they exclaim."
            self.first_meeting=False
            print(interaction_dialogue)
            return


        if self.static:
            dialogue=self.name+" mumbles something to himself."
            print(dialogue)
            return
        rng_dialogue=random.randint(0,len(self.dialogues)-1)

        dialogue_used=self.dialogues[rng_dialogue]

        interaction_dialogue=self.name+" looks at you in confusion.\n"
        interaction_dialogue=interaction_dialogue+"\""+dialogue_used+"\" they exclaim."
        print(interaction_dialogue)

        return




        


class GNPC(NPC):
    def __init__(self, room_name, description,current_room,dialogues,gift):
        super().__init__(room_name,description,current_room,dialogues)
        
        self.gift=gift


    def gift_success(self,current_game_state):

        for room in current_game_state.rooms_list:

            doors=room.connected_doors

            for i in range(len(doors)):
                if doors[i]=="NULL":
                    continue

                else:
                    doors[i]='solved'

        txt=self.name+" has unlocked all the doors in the area due to your generous gift."

        self.static=True
        
        print(txt)












