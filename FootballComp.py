class FootballComp:
    def __init__(self, CompID, SeasonID, Code):
        self.FootballCompID = CompID
        self.FootballSeasonID = SeasonID
        self.FootballCode = Code

    def UpdateFootballComp (self, compID, SeasonID, Code):
        self.FootballSeasonID = SeasonID
        self.FootballCode = Code
