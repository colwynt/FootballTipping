#
import csv
class FootballComp:
    def __init__(self, CompID, SeasonID, CompName):
        self.FootballCompID = CompID
        self.FootballSeasonID = SeasonID
        self.FootballCompName = CompName

    def UpdateFootballComp (self, CompID, SeasonID, CompName):
        self.FootballCompID = CompID
        self.FootballSeasonID = SeasonID
        self.FootballCompName = CompName

    def addCompetition(self, AllComps_addCompetition, thisFootballComp_Object_addCompetition, compID, seasonID, compName):
        AllComps_addCompetition
        thisFootballComp_Object_addCompetition
        # Add competition details to end of competition list
        AllComps_addCompetition.append([compID, seasonID, compName])
        # Delete then recreate thisFootballSeason object
        del thisFootballComp_Object_addCompetition
        thisFootballComp_Object_addCompetition = FootballComp( compID, seasonID, compName )

        return thisFootballComp_Object_addCompetition, AllComps_addCompetition

    def writeCompetitionToFile(self, AllComps_writeCompToFile):
        # Now write AllSeasons to the file
        csv_filename = './Data/FootballCompetitions.csv'  # the permanent data file of football comps
    #    AllSeasons_writeSeasonToFile
        with open( csv_filename, 'w' ) as fw:
            writer = csv.writer( fw )
            for data_list in AllComps_writeCompToFile:
                writer.writerow( data_list )