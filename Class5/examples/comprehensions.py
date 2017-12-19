def comprehension(keys, values):
    return {keys[i]: values[i] for i in range(len(keys))}

cities = ["Boston", "Los Angeles", "Toronto", "Edmonton", "Philadelphia"]
teams = ["Bruins", "Kings", "Leafs", "Oilers", "Flyers"]

nhl_teams = comprehension(cities, teams)

print(nhl_teams)
