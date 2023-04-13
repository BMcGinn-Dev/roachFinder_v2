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
spread_options = [    ["dallascowboys", 0],
    ["tampabaybuccaneers", 0],
    ["minnesotavikings", 0],
    ["cincinnatibengals", 0],
    ["buffalobills", 0],
    ["pittsburghsteelers", 0],
    ["tennesseetitans", 0],
    ["arizonacardinals", 0],
    ["houstontexans", 0],
    ["jacksonvillejaguars", 0],
    ["losangeleschargers", 0],
    ["kansascitychiefs", 0],
    ["philadelphiaeagles", 0],
    ["atlantafalcons", 0],
    ["chicagobears", 0],
    ["detroitlions", 0],
    ["newyorkjets", 0],
    ["newyorkgiants", 0],
    ["washingtoncommanders", 0],
    ["baltimoreravens", 0],
    ["miamidolphins", 0],
    ["newenglandpatriots", 0],
    ["carolinapanthers", 0],
    ["neworleanssaints", 0],
    ["lasvegasraiders", 0],
    ["denverbroncos", 0],
    ["seattleseahawks", 0],
    ["greenbaypackers", 0],
    ["losangelesrams", 0],
    ["sanfrancisco49ers", 0],
    ["indianapoliscolts", 0],
    ["clevelandbrowns", 0]
]


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
print(pairs)