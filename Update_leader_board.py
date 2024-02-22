import random
import time
import json

def UpdateLeaderBoard(username,wpm):
    
    #json--python dict
    # with open("LeaderBoard.json","r") as f:
    #     leaderboard = json.load(f)
    try:
        with open("LeaderBoard.json","r") as f:
            leaderboard = json.load(f)
    
    except FileNotFoundError: #To handle the Error of empty file
        leaderboard = {}
    
    leaderboard[username] = wpm
    
    #sort
    leaderboard = dict(sorted(leaderboard.items(),key = lambda item:item[1] ,reverse=True) )

    #python-dict ==>json
    with open ("LeaderBoard.json","w") as g:
        json.dump(leaderboard,g)