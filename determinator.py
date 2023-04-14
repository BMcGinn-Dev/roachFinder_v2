import scraperV1
import re
import pandas as pd


full_team_list_formatted = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 
                  'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 
                  'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Los Angeles Chargers', 
                  'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Philadelphia Eagles', 
                  'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Commanders']




team_list_shortened = ['Cardinals', 'Falcons', 'Ravens', 'Bills', 'Panthers', 'Bears', 
                  'Bengals', 'Browns', 'Cowboys', 'Broncos', 'Lions', 'Packers', 
                  'Texans', 'Colts', 'Jaguars', 'Chiefs', 'Raiders', 'Chargers', 
                  'Rams', 'Dolphins', 'Vikings', 'Patriots', 'Saints', 'Giants', 'Jets', 'Eagles', 
                  'Steelers', '49ers', 'Seahawks', 'Buccaneers', 'Titans', 'Commanders']



# <-- This is where you would import the final df from scraper.py -->
# for this example I will just manually fill it

# WOULD BE something like this
#scrape_df = scraper.df

#for testing

scrape_df = scraperV1.fin_result_df

#print(fin_result_df)



res_str_list = []
names = []
win_lose_spr = []


for ind in scrape_df.index:
    #Setting vars based upon df results
    winner = scrape_df['Winner'][ind]
    loser = scrape_df['Loser'][ind]
    spread = scrape_df['Spread'][ind]

    #Replaces df names w/ aesthetic names... probs couldve made this a useful def but oh well
    for name in full_team_list_formatted:
        temp_name = name.lower()
        temp_name.strip()
        temp_name = re.sub(" ", "", temp_name)
        if winner == temp_name:
            winner = name
        elif loser == temp_name:
            loser = name
    res_str = "The {0} will beat the {1} by: {2}".format(winner, loser, spread)
    res_str_list.append(res_str)
    win_lose_spr.append([winner, loser, spread])
    
#print(res_str_list)
#print(win_lose_spr)