
import json

def import_gameMsg(gameMsg_filename):


    with open(gameMsg_filename,'r',encoding='utf-8') as gameMsg_json:
        data_dict=json.load(gameMsg_json)
        introduction = data_dict["introduction"]
        youDied = data_dict["youDied"]
        youWinMinimal = data_dict["youWinMinimal"]
        youWinBestEnding = data_dict["youWinBestEnding"]
        print(introduction)

    return



game_json="gameMsg.json"

import_gameMsg(game_json)
