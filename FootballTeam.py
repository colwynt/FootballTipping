#
import csv
class FootballTeam:
    def __init__(self, TeamID, CompID, SeasonID, TeamName):
        self.FootballTeamID = TeamID
        self.FootballCompID = CompID
        self.FootballSeasonID = SeasonID
        self.FootballTeamName = TeamName

    def UpdateFootballTeam (self, TeamID, CompID, SeasonID, TeamName):
        self.FootballTeamID = TeamID
        self.FootballSeasonID = SeasonID
        self.FootballCompID = CompID
        self.FootballTeamName = TeamName

    def addTeam(self, AllTeams_addTeam, thisFootballTeam_Object_addTeam, teamID, compID, seasonID, teamName):
        AllTeams_addTeam
        thisFootballTeam_Object_addTeam
        # Add team details to end of team list
        AllTeams_addTeam.append( [teamID, compID, seasonID, teamName] )
        # Delete then recreate thisFootballTeam object
        del thisFootballTeam_Object_addTeam
        thisFootballTeam_Object_addTeam = FootballTeam( teamID, compID, seasonID, teamName )

        return thisFootballTeam_Object_addTeam, AllTeams_addTeam

    def writeTeamToFile(self, AllTeams_writeTeamToFile):
        # Now write AllSeasons to the file
        csv_filename = './Data/FootballTeams.csv'  # the permanent data file of football comps
        #    AllSeasons_writeTeamToFile
        with open( csv_filename, 'w' ) as fw:
            writer = csv.writer( fw )
            for data_list in AllTeams_writeTeamToFile:
                writer.writerow( data_list )