import requests
import fastf1 as ff1

ff1.Cache.enable_cache('cache')

def get_drivers_standings():
    url = "https://ergast.com/api/f1/current/driverStandings.json"
    response = requests.get(url)
    data = response.json()
    drivers_standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']  # noqa: E501
    return drivers_standings

def calculate_max_points_for_remaining_season():
    POINTS_FOR_SPRINT = 8 + 25 + 1  # Winning the sprint, race and fastest lap
    POINTS_FOR_CONVENTIONAL = 25 + 1  # Winning the race and fastest lap

    events = ff1.events.get_events_remaining()
    # Count how many sprints and conventional races are left
    sprint_events = \
        len(events.loc[events["EventFormat"] == "sprint"])
    conventional_events = \
        len(events.loc[events["EventFormat"] == "conventional"])

    # Calculate points for each
    sprint_points = sprint_events * POINTS_FOR_SPRINT
    conventional_points = conventional_events * POINTS_FOR_CONVENTIONAL

    return sprint_points + conventional_points

def calculate_who_can_win(driver_standings, max_points):
    LEADER_POINTS = int(driver_standings[0]['points'])

    for _, driver in enumerate(driver_standings):
        driver_max_points = int(driver["points"]) + max_points
        can_win = 'Não' if driver_max_points < LEADER_POINTS else 'Sim'

        print(f"{driver['position']}: \
{driver['Driver']['code']}, \
Pontuação Atual: {driver['points']}, \
Pontuação máxima que pode alcançar: {driver_max_points}, \
Pode ser campeão: {can_win}")

# Get the current drivers standings
driver_standings = get_drivers_standings()

# Get the maximum amount of points
points = calculate_max_points_for_remaining_season()

# Print which drivers can still win
calculate_who_can_win(driver_standings, points)

