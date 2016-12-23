import os
import itertools
from random import shuffle

players = ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9']

# Generate teams
teams = list(itertools.combinations(players, 2))
print('')
print('Teams:')
for team in teams:
	print(team)
print('Number of teams are: ' +str(len(teams)))

# Generate games
games = []
print('')
for i in range(0, len(teams)):
	for j in range(i, len(teams)):
		if len(set(teams[i]) ^ set(teams[j])) == 4:
			games.append([teams[i], teams[j]])

print("Unfiltered number of games: " +str(len(games)))

# Filter games
shuffle(games)
pickedGames = []
pickedTeams = []
def IsValidGamePicks(game):
	team1 = game[0]
	team2 = game[1]
	# Does the team already exist?
	if any(team1 == t for t in pickedTeams):
		return False
	if any(team2 == t for t in pickedTeams):
		return False
	return True

occurrences = { key:0 for key in players }
for game in games:
	if IsValidGamePicks(game):
		pickedGames.append(game)
		pickedTeams.append(game[0])
		pickedTeams.append(game[1])
		occurrences[game[0][0]] = occurrences[game[0][0]] + 1
		occurrences[game[0][1]] = occurrences[game[0][1]] + 1
		occurrences[game[1][0]] = occurrences[game[1][0]] + 1
		occurrences[game[1][1]] = occurrences[game[1][1]] + 1

print("Occurrences for each player:")
print(occurrences)

# Let's shuffle it up!
shuffle(pickedGames)

# Dump the games to file
f = open("foosball.txt", "w")
for game in pickedGames:
	f.write(str(game[0]) +' vs ' +str(game[1]) +'\r\n')
f.close()
