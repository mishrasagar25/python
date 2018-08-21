from random import choice
players = [];
team_name = {};

file = open('players.txt','r')
players = file.read().splitlines()

print("enter two team name : ")
team_name[input()] = []
team_name[input()] = []

while (len(players)>0):
    player_a = choice(players)
    str = list(team_name.keys())[0]
    team_name[str].append(player_a)
    players.remove(player_a)
    #print(players)
    if(len(players)<=0):
        break;
    player_b = choice(players)
    str2 = list(team_name.keys())[1]
    team_name[str2].append(player_b)
    players.remove(player_b)
    #print(players)

print(team_name)


