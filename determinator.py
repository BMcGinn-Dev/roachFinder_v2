#import scraper
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
fin_result_data = [['dallascowboys', 'tampabaybuccaneers', 3.292, 25.8155, 22.5235, 48.339], ['cincinnatibengals', 'minnesotavikings', 6.724, 31.3975, 24.6735, 56.071], ['buffalobills', 'pittsburghsteelers', 7.585, 29.2515, 21.6665, 50.918], ['arizonacardinals', 'tennesseetitans', 0.534, 24.8275, 24.293499999999998, 49.120999999999995], ['jacksonvillejaguars', 'houstontexans', 10.117, 32.0745, 21.9585, 54.033], ['kansascitychiefs', 'losangeleschargers', 5.18, 28.338499999999996, 23.1585, 51.497], ['philadelphiaeagles', 'atlantafalcons', 11.514, 34.2235, 22.7095, 56.933], ['detroitlions', 'chicagobears', 4.74, 30.1295, 25.3905, 55.519999999999996], ['newyorkjets', 'newyorkgiants', 2.107, 25.819499999999998, 23.7125, 49.532], ['baltimoreravens', 'washingtoncommanders', 5.442, 28.234499999999997, 22.7925, 51.027], ['miamidolphins', 'newenglandpatriots', 0.507, 25.153499999999998, 24.6465, 49.8], ['neworleanssaints', 'carolinapanthers', 5.172, 28.3915, 23.2195, 51.611000000000004], ['denverbroncos', 'lasvegasraiders', 1.512, 24.2045, 22.6925, 46.897], ['greenbaypackers', 'seattleseahawks', 1.836, 25.4305, 23.5945, 49.025], ['sanfrancisco49ers', 'losangelesrams', 12.181, 33.8475, 21.6665, 55.513999999999996], ['clevelandbrowns', 'indianapoliscolts', 5.092, 27.8545, 22.7625, 50.617000000000004]]
fin_result_df = df = pd.DataFrame(fin_result_data, columns=['Winner', 'Loser', 'Spread', 'Winner Total', 'Loser Total', 'Over_Under'])

#print(fin_result_df)

scrape_df = fin_result_df

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
print(win_lose_spr)