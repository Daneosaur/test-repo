#!usr/bin/env python3.10

from bs4 import BeautifulSoup
import requests
from sportsipy.nfl.boxscore import Boxscore
from sportsipy.nfl.teams import Teams


r = requests.get('https://www.pro-football-reference.com/years/2022/opp.htm')

print(r.headers)

teams = Teams()
colts = teams('CLT')
kansas = teams('KAN')
pit = teams('PIT')
cle = teams('CLE')

kanSRS = kansas.simple_rating_system
coltSRS = colts.simple_rating_system

spread = kanSRS - coltSRS
#print(kansas.dataframe)

# for team in teams:
#     print(team.name)  # Prints the team's name
#     # Prints the team's average margin of victory
#     print("MOV" + str(team.margin_of_victory))
#     print("YPP" + str(team.yards_per_play))
#     print("SRS" + str(team.simple_rating_system))