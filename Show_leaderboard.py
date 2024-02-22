import json

def ShowLeaderBoard():
    with open ("LeaderBoard.json","r") as f : 
        leaderboard=json.load (f)
    return leaderboard