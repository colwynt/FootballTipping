class FootballSeason:
    def __init__(self, seasonID, compID, startDate, endDate, numberGames, numberTeams):
        self.SeasonID = seasonID
        self.SeasonFootballCompID = compID
        self.SeasonStartDate = startDate
        self.SeasonEndDate = endDate
        self.SeasonNumberGames = numberGames
        self.SeasonNumberTeams = numberTeams

    def addTeam(self):
        self.SeasonNumberTeams = +1

    def addGame(self):
        self.SeasonNumberGames = +1
