teams = [{'team': 'Real Madrid', 'year': 1902},
         {'team': 'Bate', 'year': 1973},
         {'team': 'Manchester United', 'year': 1878},
         {'team': 'Bayern Munchen', 'year': 1900},
         {'team': 'Barcelona', 'year': 1899},
         {'team': 'Milan', 'year': 1899}]


def search_team(foundation_year, teams):
    founded_teams = []
    for team in teams:
        if team['year'] == foundation_year:
            founded_teams.append(team['team'])
    if founded_teams:
        return founded_teams
    else:
        return 'No teams'


result = search_team(1899, teams)
print result
