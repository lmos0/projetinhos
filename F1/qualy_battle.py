import pandas as pd
import requests

import fastf1 as ff1
from fastf1 import plotting

import seaborn as sns
import matplotlib.pyplot as plt

def ergast_retrieve(api_endpoint: str):
    url = f'https://ergast.com/api/f1/{api_endpoint}.json'
    response = requests.get(url).json()
    
    return response['MRData']

# By changing these params you can easily get other seasons 
season = 2022

all_quali_results = pd.DataFrame()

# We want this so that we know which driver belongs to which team, so we can color them later
team_drivers = {}

current_round = 1

all_quali_results = pd.DataFrame()

# We want this so that we know which driver belongs to which team, so we can color them later
team_drivers = {}

# [Line 6] Since we’ll be looping through every race weekend (‘round’), we obviously start with the first one. 
# The variable current_round will increase once we iterate over all the weekends, 
# so our script will know what session to retrieve.
 
current_round = 1

# Since we will make sure our script can retrieve the qualifying battles from any season, 
# we obviously don’t know how many races have been in that specific season. 
# For example, we know that the 2021 season contained 22 races.

# So, what we will do is we initiate an infinite loop by running while True: 
# which will keep on running indefinitely since it is always true. 
# If we at some point stop receiving new qualifying results while looping through all the races of the specified season,
# we break the loop by calling break .

while True:
    # We request the qualifying results of the current round from Ergast
    race = ergast_retrieve(f'{season}/{current_round}/qualifying')
    
    # If session doesn't exist, cancel loop
    if not race['RaceTable']['Races']:
        break
    #  We store the qualifying results in a variable called results 
    # and we create a dictionary called quali_results where we store our processed results in
    results = race['RaceTable']['Races'][0]['QualifyingResults']

    quali_results = {'round': current_round}

    # We initiate a loop that goes through every single finishing position. 
    for j in range(len(results)):
        # We extract the information we need and we store it in some variables
        driver = results[j]['Driver']['code']
        position = int(results[j]['position'])
        team = results[j]['Constructor']['name']
        
        #  If a driver needs to be excluded, like Kubica, 
        # we run continue which skips the current iteration of the loop and moves on to the next driver
        #if driver in drivers_to_exclude:
            #continue
        
        # Create mapping for driver - team
        if not team in team_drivers:
            team_drivers[team] = [driver]
        else:
            if not driver in team_drivers[team]:
                team_drivers[team].append(driver)
                
        quali_results[driver] = position
            
    all_quali_results = all_quali_results.append(quali_results, ignore_index=True)
    
    current_round += 1

# Now we want to know, per round, per team, who qualified higher?
all_quali_battle_results = []
team_colors_palette = []

for team in team_drivers:
    drivers = team_drivers[team]
    
    quali_results = all_quali_results[drivers]
    
    # We do dropna() to only include the sessions in which both drivers participated
    fastest_driver_per_round = quali_results.dropna().idxmin(axis=1)
    
    quali_battle_result = fastest_driver_per_round.value_counts().reset_index()
    
    for _, driver in quali_battle_result.iterrows():
        all_quali_battle_results.append({
            'driver': driver['index'],
            'team': team,
            'quali_score': driver[0]
        })
    
    team_colors_palette.append(ff1.plotting.team_color(team))
    # If none, replace None with grey
    team_colors_palette = ['#D3D3D3' if v is None else v for v in team_colors_palette]


# Finally, convert to a DataFrame so we can plot
all_quali_battle_results = pd.DataFrame.from_dict(all_quali_battle_results)

# Increase the size of the plot 
sns.set(rc={'figure.figsize':(11.7,8.27)})

# Create custom color palette
custom_palette = sns.set_palette(sns.color_palette(team_colors_palette))

fig, ax = plt.subplots()

ax.set_title(f"{season} Disputa Interna em Classificação")

g = sns.barplot(
    x='driver',
    y='quali_score', 
    hue='team',
    data=all_quali_battle_results, 
    dodge=False,
    palette=custom_palette,
)

plt.yticks(range(max(all_quali_battle_results['quali_score']) + 1))

plt.legend([],[], frameon=False)

g.set(xlabel=None)
g.set(ylabel=None)

plt.savefig('qualifying_battles_2022.png')

plt.show()