class FootballTeam:
    def __init__(self, CompID, SeasonID, TeamID, TeamName):
        self.FootballTeamID = TeamID
        self.FootballCompID = CompID
        self.FootballSeasonID = SeasonID
        self.FootballTeamName = TeamName

    def UpdateFootballTeam (self, CompID, SeasonID, TeamID, TeamName):
        self.FootballTeamID = TeamID
        self.FootballSeasonID = SeasonID
        self.FootballCompID = CompID
        self.FootballTeamName = TeamName

    def AddFootballTeam (self, CompID, SeasonID, TeamID, TeamName):
        self.FootballTeamID = TeamID
        self.FootballSeasonID = SeasonID
        self.FootballCompID = CompID
        self.FootballTeamName = TeamName