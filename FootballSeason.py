import csv
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

        return

    def addGame(self):
        self.SeasonNumberGames = +1

        return

    def addSeason(self, AllSeasons_addSeason, thisFootballSeason_Object_addSeason, seasonID, compID, startDate, endDate, numberGames, numberTeams):
        AllSeasons_addSeason
        thisFootballSeason_Object_addSeason
        # Add season details to end of season list
        AllSeasons_addSeason.append([seasonID, compID, startDate, endDate, numberGames, numberTeams])
        # Delete then recreate thisFootballSeason object
        del thisFootballSeason_Object_addSeason
        thisFootballSeason_Object_addSeason = FootballSeason( seasonID, compID, startDate, endDate, numberGames, numberTeams )

        return thisFootballSeason_Object_addSeason, AllSeasons_addSeason

    def writeSeasonToFile(self, AllSeasons_writeSeasonToFile):
        # Now write AllSeasons to the file
        csv_filename = './Data/FootballSeasons.csv'  # the permanent data file of football seasons
    #    AllSeasons_writeSeasonToFile
        with open( csv_filename, 'w' ) as fw:
            writer = csv.writer( fw )
            for data_list in AllSeasons_writeSeasonToFile:
                writer.writerow( data_list )
        return
