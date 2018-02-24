#basic class structure
class Horse:

    def __init__(self, name, gender, breeder, trainer, races, wins, place, show):
        self.name = name
        self.gender = gender
        self.breeder = breeder
        self.trainer = trainer
        self.races = races
        self.wins = wins
        self.place = place
        self.show = show


racehorse = Horse(
    "California Chrome",
    "Male",
    "Perry Martin",
    "Art Sherman",
    27,
    16,
    4,
    1
)


#play around with the class
racehorse.races = 28
print(racehorse.races)
print(racehorse.wins)
print('winning percentage: %.1f' % (racehorse.wins/float(racehorse.races) * 100))
