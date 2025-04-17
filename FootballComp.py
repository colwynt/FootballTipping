class FootballComp:
    def __init__(self, CompID, SeasonID, CompName):
        self.FootballCompID = CompID
        self.FootballSeasonID = SeasonID
        self.FootballCompName = CompName

    def UpdateFootballComp (self, CompID, SeasonID, CompName):
        self.FootballCompID = CompID
        self.FootballSeasonID = SeasonID
        self.FootballCompName = CompName
