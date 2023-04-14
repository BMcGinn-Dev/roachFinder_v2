
import spread_scraperV1
import determinator

spread_options = spread_scraperV1.spread_options
win_lose_spr = determinator.win_lose_spr


full_team_list_formatted = spread_scraperV1.full_team_list_formatted

#Creating the 'quad' list with the following values
#quad --> [winnerName, loserName, calculatedSpread, winnerSpreadChoice, loserSpreadChoice]

quad = []
#print(spread_options)

for trio in win_lose_spr:
    winner = trio[0].lower().strip().replace(" ", "")
    loser = trio[1].lower().strip().replace(" ", "")
    
    #print(winner, loser)
    
    temp = [winner, loser, trio[2], 0, 0]
    
    
    for team in spread_options:
        win2 = team[0].lower().strip().replace(" ", "")
        los2 = team[0].lower().strip().replace(" ", "")
        
        if win2 == winner:
            temp[3] = team[1]
        if los2 == loser:
            temp[4] = team[1]
        
    quad.append(temp)


#_____________________________________________________________________----
#Logic to determine if spread gets covered

spread_decisions = []
formatted_choices = []

for decision in quad:
    winner = decision[0]
    loser = decision[1]
    cSpr = decision[2]
    wSpr = decision[3]
    lSpr = decision[4]
    
    base = 100
    winner_total = base + cSpr
    loser_total = base + lSpr
    
    if loser_total > winner_total:
        #print(f'Loser covers --> {loser} ----> cSpr: {cSpr}, lSpr: {lSpr}')
        spread_decisions.append([loser, lSpr])
    elif winner_total > loser_total:
        #print(f'Winner covers --> {winner} ----> cSpr: {cSpr}, wSpr: {wSpr}')
        spread_decisions.append([winner, wSpr])
    else:
        #print("Its a tie")
        spread_decisions.append(["MONEYLINE", 0])
        
        

#print(spread_decisions)

#_____________________________________________________________________----
# Now this is a really, really bad way to format the names in terms of big O notation

for pair in spread_decisions:
    name = pair[0]
    for teamName in full_team_list_formatted:
            formatted = teamName
            teamName = teamName.lower()
            teamName = str(teamName)
            teamName = teamName.replace(" ", "")
            #print(f'FORMATTED: {formatted}, TEAMNAME: {teamName}')
            if name == teamName:
                name = formatted
    formatted_choices.append([name, pair[1]])



#for choice in formatted_choices:
#    print(choice, '\n')

form_choices = formatted_choices
    



    
    
    