#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re, pandas as pd, bs4, requests
import spread_scraperV1


# How this is supposed to go:

# Step 1: Scrape the data from the urls --> DONE
# Step 2: Put all the data into a tri-dimensional list [[[]]] --> DONE
# Step 3: Determine weekly matchups: (CANT DO THIS YET)
# Step 4: Based on those matchups, run the calculations: (DONE)
# Step 5: Return the results: DONE (Returned in datafram named fin_result_df)
# Step 6: Compare them to the spread & output the winner:


# In[2]:


#Step 1: Scraping the data from the urls

full_team_list = ['arizonacardinals', 'atlantafalcons', 'baltimoreravens', 'buffalobills', 'carolinapanthers', 'chicagobears', 
                  'cincinnatibengals', 'clevelandbrowns', 'dallascowboys', 'denverbroncos', 'detroitlions', 'greenbaypackers', 
                  'houstontexans', 'indianapoliscolts', 'jacksonvillejaguars', 'kansascitychiefs', 'lasvegasraiders', 'losangeleschargers', 
                  'losangelesrams', 'miamidolphins', 'minnesotavikings', 'newenglandpatriots', 'neworleanssaints', 'newyorkgiants', 'newyorkjets', 'philadelphiaeagles', 
                  'pittsburghsteelers', 'sanfrancisco49ers', 'seattleseahawks', 'tampabaybuccaneers', 'tennesseetitans', 'washington']

#I needed this bc for the matchup creator i used 'washington' but the spread scrape was 'commanders'
full_team_list2 = ['arizonacardinals', 'atlantafalcons', 'baltimoreravens', 'buffalobills', 'carolinapanthers', 'chicagobears', 
                  'cincinnatibengals', 'clevelandbrowns', 'dallascowboys', 'denverbroncos', 'detroitlions', 'greenbaypackers', 
                  'houstontexans', 'indianapoliscolts', 'jacksonvillejaguars', 'kansascitychiefs', 'lasvegasraiders', 'losangeleschargers', 
                  'losangelesrams', 'miamidolphins', 'minnesotavikings', 'newenglandpatriots', 'neworleanssaints', 'newyorkgiants', 'newyorkjets', 'philadelphiaeagles', 
                  'pittsburghsteelers', 'sanfrancisco49ers', 'seattleseahawks', 'tampabaybuccaneers', 'tennesseetitans', 'washingtoncommanders']

urls = ['https://www.espn.com/nfl/stats/team/_/table/passing/sort/netYardsPerGame/dir/desc'
       , 'https://www.espn.com/nfl/stats/team/_/table/passing/sort/netPassingYardsPerGame/dir/desc'
       , 'https://www.espn.com/nfl/stats/team/_/table/rushing/sort/rushingYardsPerGame/dir/desc'
       , 'https://www.espn.com/nfl/stats/team/_/table/passing/sort/totalPointsPerGame/dir/desc'
       , 'https://www.espn.com/nfl/stats/team/_/view/defense/table/passing/sort/netYardsPerGame/dir/asc'
       , 'https://www.espn.com/nfl/stats/team/_/view/defense/table/passing/sort/netPassingYardsPerGame/dir/asc'
       , 'https://www.espn.com/nfl/stats/team/_/view/defense/table/rushing/sort/rushingYardsPerGame/dir/asc'
       , 'https://www.espn.com/nfl/stats/team/_/view/defense/table/passing/sort/totalPointsPerGame/dir/asc']

offensive_results_list = []
offensive_stats_list = []

TEAM_TOTAL_SUBTRACTOR = 6.3335

#creates list of results from scrape
def fill_results_list():
    
    for url in urls:
        target_url = url
        
        #In case you begin to get an SSL Certificate are, change to this --> r = request.get(target_url, veryify=False)
        r = requests.get(target_url)
        content = r.content
        content = content.decode('utf-8')
        soup = bs4.BeautifulSoup(content, features="html.parser")

        soup_str = str(soup)

        result = re.search('<tbody class="Table__TBODY">(.*)</tbody>', soup_str)
        table_body = result.group(1)
        table_body = table_body.split('>')

        item_list = []
        team_rank_list = []
        team_list = []
        rank = 1

        for item in table_body:
            if "title=" and '<img class=' in item:
                item_list.append(item)

        for item in item_list:
            search_res = re.search('title="(.*)"', item)
            team_name = search_res.group(1).lower()
            team_name = re.sub(' ', '', team_name)
            team_list.append(team_name)

        for team in team_list:
            team_rank_list.append([team, rank])
            rank += 1

        #print(team_rank_list)
        offensive_results_list.append(team_rank_list)
        #print("ADDED -------------")
        #print(offensive_results_list)


# In[3]:


#Step 2: Putting all the data into a tri-dimensional list [[[]]]

#Each definition returns a list of pairs relating the team name to its relative rank
def get_offensive_stats():
    
    #offensive_stats_list = []
    
    typgr = 0
    tpypgr = 0
    trypgr = 0
    tppgr = 0
    def_typgr = 0
    def_tpypgr = 0
    def_trypgr = 0
    def_tppgr = 0

    #probs need to rename the list variable
    typg_ranks = offensive_results_list[0]
    tpypg_ranks = offensive_results_list[1]
    trypg_ranks = offensive_results_list[2]
    tppg_ranks = offensive_results_list[3]
    tppy_ranks_def = offensive_results_list[4]
    tpypy_ranks_def = offensive_results_list[5]
    trypy_ranks_def = offensive_results_list[6]
    tppg_ranks_def = offensive_results_list[7]


    #print(temp_typgr)
    for team in full_team_list:
        # loop to get total yards per game rank
        for pair in typg_ranks:
            if pair[0] == team:
                rank = pair[1]
                typgr = rank
        # loop to get total passing yards per game rank        
        for pair in tpypg_ranks:
            if pair[0] == team:
                rank = pair[1]
                tpypgr = rank
        # loop to get total rushing yards per game rank       
        for pair in trypg_ranks:
            if pair[0] == team:
                rank = pair[1]
                trypgr = rank
        # loop to get total rushing yards per game rank       
        for pair in tppg_ranks:
            if pair[0] == team:
                rank = pair[1]
                tppgr = rank
        # loop to get total yards per game allowed by the defense rank
        for pair in tppy_ranks_def:
            if pair[0] == team:
                rank = pair[1]
                def_typgr = rank
        # loop to get total yards per game allowed by the defense rank
        for pair in tpypy_ranks_def:
            if pair[0] == team:
                rank = pair[1]
                def_tpypgr = rank
        for pair in trypy_ranks_def:
            if pair[0] == team:
                rank = pair[1]
                def_trypgr = rank
                
        for pair in tppg_ranks_def:
            if pair[0] == team:
                rank = pair[1]
                def_tppgr = rank
                
        #print("The {0} offense has a total yard rank of {1} \n a passing yard rank of {2} \n a rushing yard rank of {3} \n a total points rank of {4}"
         #     .format(team, typgr, tpypgr, trypgr, tppgr))
        
        offensive_stats = [team, typgr, tpypgr, trypgr, tppgr, def_typgr, def_tpypgr, def_trypgr, def_tppgr]
    
        offensive_stats_list.append(offensive_stats)
        
    res = []
    for i in offensive_stats_list:
        if i not in res:
            res.append(i)

    return res
        
fill_results_list()
res = get_offensive_stats()
#print(res)


# In[4]:


#Step 3: get the matchups: (we cant actually do this yet)

#Need to fill the matchups.txt file in the proper format

#dallascowboys,tampabaybuccaneers
#greenbaypackers,chicagobears
#miamidolphins,atlantafalcons

#Getting the matchups from Include/matchups.txt
matchups = spread_scraperV1.matchups
matchups_length = len(matchups)
#print(matchups)

#commenting out .txt file method
'''
try:
    with open('./matchups.txt', 'r') as f:
        for line in f:
            matchups.append(line)
        f.close()
except FileNotFoundError:
    print("We didnt find the matchups.txt file you tried to generate")

matchups = [s.rstrip() for s in matchups]

#print(matchups_length)

'''

#print(len(res))


# In[5]:


# Step 4a: defs to run the calculations

#Does all the calculations for each pair
def get_spread():
    team_A_total = 0
    team_B_total = 0
    
    # Comparing total yards for team A to total yards allowed by team B
    ratioTYF_a = (13.5 * (1 + (1 - (a_typgr/ 32))))
    ratioTYA_b = (13.5 * (1 + (1 - (b_def_typgr / 32))))

    if (ratioTYF_a > ratioTYA_b):
        t = ratioTYF_a / ratioTYA_b
        team_A_total += (3.5 * t)
        team_B_total += 3.5
    else:
        t = ratioTYA_b / ratioTYF_a
        team_B_total += (3.5 * t)
        team_A_total += 3.5


    # Comparing total yards for team B to total yards allowed by team A
    ratioTYF_a = (13.5 * (1 + (1 - (a_def_typgr/ 32))))
    ratioTYA_b = (13.5 * (1 + (1 - (b_typgr / 32))))

    if (ratioTYF_a > ratioTYA_b):
        t = ratioTYF_a / ratioTYA_b
        team_A_total += (3.5 * t)
        team_B_total += 3.5
    else:
        t = ratioTYA_b / ratioTYF_a
        team_B_total += (3.5 * t)
        team_A_total += 3.5
        
        
    # Comparing total passing yards for team A to total passing yards allowed by team B
    ratioTPYF_a = (13.5 * (1 + (1 - (a_tpypgr/ 32))))
    ratioTPYA_b = (13.5 * (1 + (1 - (b_def_tpypgr / 32))))

    if (ratioTPYF_a > ratioTPYA_b):
        t = ratioTPYF_a / ratioTPYA_b
        team_A_total += (3.5 * t)
        team_B_total += 3.5
    else:
        t = ratioTPYA_b / ratioTPYF_a
        team_B_total += (3.5 * t)
        team_A_total += 3.5
        
        
    # Comparing total passing yards for team B to total passing yards allowed by team A
    ratioTPYF_a = (13.5 * (1 + (1 - (a_def_tpypgr/ 32))))
    ratioTPYA_b = (13.5 * (1 + (1 - (b_tpypgr / 32))))

    if (ratioTPYF_a > ratioTPYA_b):
        t = ratioTPYF_a / ratioTPYA_b
        team_A_total += (3.5 * t)
        team_B_total += 3.5
    else:
        t = ratioTPYA_b / ratioTPYF_a
        team_B_total += (3.5 * t)
        team_A_total += 3.5
        
        
        
    # Comparing total rushing yards for team A to total rushing yards allowed by team B
    ratioTRYF_a = (13.5 * (1 + (1 - (a_trypgr/ 32))))
    ratioTRYA_b = (13.5 * (1 + (1 - (b_def_trypgr / 32))))

    if (ratioTRYF_a > ratioTRYA_b):
        t = ratioTRYF_a / ratioTRYA_b
        team_A_total += (3.5 * t)
        team_B_total += 3.5
    else:
        t = ratioTRYA_b / ratioTRYF_a
        team_B_total += (3.5 * t)
        team_A_total += 3.5
        
    # Comparing total rushing yards for team B to total rushing yards allowed by team A
    ratioTRYF_a = (13.5 * (1 + (1 - (a_def_trypgr/ 32))))
    ratioTRYA_b = (13.5 * (1 + (1 - (b_trypgr / 32))))

    if (ratioTRYF_a > ratioTRYA_b):
        t = ratioTRYF_a / ratioTRYA_b
        team_A_total += (3.5 * t)
        team_B_total += 3.5
    else:
        t = ratioTRYA_b / ratioTRYF_a
        team_B_total += (3.5 * t)
        team_A_total += 3.5
        
        
    # Comparing total points for team A to total points allowed by team B
    ratioTPF_a = (13.5 * (1 + (1 - (a_tppgr/ 32))))
    ratioTPA_b = (13.5 * (1 + (1 - (b_def_tppgr / 32))))

    if (ratioTPF_a > ratioTPA_b):
        t = ratioTPF_a / ratioTPA_b
        team_A_total += (3.5 * t)
        team_B_total += 3.5
    else:
        t = ratioTPA_b / ratioTPF_a
        team_B_total += (3.5 * t)
        team_A_total += 3.5
        
        
    # Comparing total points for team B to total points allowed by team A
    ratioTPF_a = (13.5 * (1 + (1 - (a_def_tppgr/ 32))))
    ratioTPA_b = (13.5 * (1 + (1 - (b_tppgr / 32))))

    if (ratioTPF_a > ratioTPA_b):
        t = ratioTPF_a / ratioTPA_b
        team_A_total += (3.5 * t)
        team_B_total += 3.5
    else:
        t = ratioTPA_b / ratioTPF_a
        team_B_total += (3.5 * t)
        team_A_total += 3.5
        
        
    return team_A_total, team_B_total

#Gets spread, winner, loser, winner score, loser score, and over/under in that order
def get_win_and_spread():

    a_total, b_total = get_spread()

    spread = abs(a_total-b_total)

    a_total = round(a_total, 3)
    b_total = round(b_total, 3)
    spread = round(spread, 3)
    winning_team = ''
    losing_team = ''


    #print("The final score will be {0} to {1}. The spread will be {2}.".format(a_total, b_total, spread))
    if a_total > b_total:
        #print("The {0} will beat the {1} by {2}".format(comp_a_name, comp_b_name, spread))
        winning_team = comp_a_name
        losing_team = comp_b_name
        winning_total = a_total - TEAM_TOTAL_SUBTRACTOR
        losing_total = b_total - TEAM_TOTAL_SUBTRACTOR
    else:
        #print("The {0} will beat the {1} by {2}".format(comp_b_name, comp_a_name, spread))
        winning_team = comp_b_name
        losing_team = comp_a_name
        winning_total = b_total - TEAM_TOTAL_SUBTRACTOR
        losing_total = a_total - TEAM_TOTAL_SUBTRACTOR
        
    return spread, winning_team, losing_team, winning_total, losing_total




def get_comp_ranks(res, index):
    
    typgr = res[index][1]
    tpypgr = res[index][2]
    trypgr = res[index][3]
    tppgr = res[index][4]
    def_typgr = res[index][5]
    def_tpypgr = res[index][6]
    def_trypgr = res[index][7]
    def_tppgr = res[index][8]
    
    return typgr, tpypgr, trypgr, tppgr, def_typgr, def_tpypgr, def_trypgr, def_tppgr


# In[6]:


#print(matchups)
fin_result_data = []

for matchup in matchups:

    temp = matchup.split(',')
    #print(temp[0], temp[1])
    comp_a_name = temp[0]
    comp_b_name = temp[1]

    comp_a_index = 0
    comp_b_index = 0

    #getting indexes of competitors team stats 
    for team in res:
        if team[0] == comp_a_name:
            index = full_team_list.index(team[0])
            comp_a_index = index

        if team[0] == comp_b_name:
            index = full_team_list.index(team[0])
            comp_b_index = index
            
    compA_ranks = get_comp_ranks(res, comp_a_index)
    compB_ranks = get_comp_ranks(res, comp_b_index)
    #print(compA_ranks)
    #print(compB_ranks)
    
    
    #Assigning team A their ranks
    a_typgr = compA_ranks[0]
    a_tpypgr = compA_ranks[1]
    a_trypgr = compA_ranks[2]
    a_tppgr = compA_ranks[3]
    a_def_typgr = compA_ranks[4]
    a_def_tpypgr = compA_ranks[5]
    a_def_trypgr = compA_ranks[6]
    a_def_tppgr = compA_ranks[7]

    #Assigning team B their ranks
    b_typgr = compB_ranks[0]
    b_tpypgr = compB_ranks[1]
    b_trypgr = compB_ranks[2]
    b_tppgr = compB_ranks[3]
    b_def_typgr = compB_ranks[4]
    b_def_tpypgr = compB_ranks[5]
    b_def_trypgr = compB_ranks[6]
    b_def_tppgr = compB_ranks[7]
    
    spread, winner, loser, winner_total, loser_total = get_win_and_spread()
    #print(spread, winner, loser, winner_total, loser_total)
    
    over_under = winner_total + loser_total

    res_data = [winner, loser, spread, winner_total, loser_total, over_under]

    fin_result_data.append(res_data)
    
    
    


# In[7]:


#print(fin_result_data)
fin_result_df = pd.DataFrame(fin_result_data, columns=['Winner', 'Loser', 'Spread', 'Winner Total', 'Loser Total', 'Over_Under'])


# In[8]:


#print(fin_result_df)


# In[ ]:




