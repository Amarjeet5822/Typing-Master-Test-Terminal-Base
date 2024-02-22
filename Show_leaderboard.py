import json

def ShowLeaderBoard():
    with open ("LeaderBoard.json","r") as file :
        leaderboard=json.load (file)
    return leaderboard #leaderboard ek dictionary hai