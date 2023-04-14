import json, pathlib, re, time, pandas as pd, bs4, requests, os

full_team_list_formatted = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 
                  'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 
                  'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Los Angeles Chargers', 
                  'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Philadelphia Eagles', 
                  'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Commanders']

url = 'https://www.sportsline.com/nfl/odds/'

#--------------------------------------------------------------------------------

r = requests.get(url)
content = r.content
content = content.decode('utf-8')
soup = bs4.BeautifulSoup(content, features="html.parser")
#print(soup.prettify)
soup_str = str(soup)
#print(soup_str)

#----------------------------------------------------------------------------------------

#HERE HER HER HERE HERE HERE HERE HERE HERE
#This is the output you're looking for with the scrape!!!!
spread_options = [['Dallas Cowboys', -4], ['Tampa Bay Buccaneers', 4], ['Cincinnati Bengals', -6], ['Minnesota Vikings', 6], ['Buffalo Bills', -3], ['Pittsburgh Steelers', 3], ['Arizona Cardinals', -5], ['Tennessee Titans', 5], ['Jacksonville Jaguars', 10], ['Houston Texans', -10], ['Kansas City Chiefs', 7], ['Los Angeles Chargers', -7], ['Philadelphia Eagles', 6], ['Atlanta Falcons', -6], ['Detroit Lions', 5], ['Chicago Bears', -5], ['New York Jets', 6], ['New York Giants', -6], ['Baltimore Ravens', 3], ['Washington Commanders', -3], ['Miami Dolphins', 8], ['New England Patriots', -8], ['New Orleans Saints', 3], ['Carolina Panthers', -3], ['Denver Broncos', 9], ['Las Vegas Raiders', -9], ['Green Bay Packers', 5], ['Seattle Seahawks', -5], ['San Francisco 49ers', 5], ['Los Angeles Rams', -5], ['Cleveland Browns', 9], ['Indianapolis Colts', -9]]


#Now I need to pair each adjacent element in the list which I already did but deleted for some reason
#These are our spread options
#print(spread_options)

pairs = []
teams_and_spreads = set()
final = []

#print(spread_options[::2])
#print(spread_options[1::2])

#Pairing every inner array in the array with its adjacent elements using the zip function (cool!)
pairing = zip(spread_options[::2], spread_options[1::2])

#print(pairing)

# Use a list comprehension to combine the pairs into one element
pairs = [x + y for x, y in pairing]
#print(pairs)