
# This is the hub Python script of the football tipping system.

# The general logic of the system is to create essential objects by gaining input from users to find out
# what season (e.g. 2025) and competition (e.g. EPL) is to be processed. Once a season and competition
# have been specified then stored information is read from text files and core objects created. Tips and
# Results can then be entered. Depending on the season and competition selected various other core information
# may also need to be entered - draws, teams, players, coaches, tippers etc. Information is written to
# text files for storage between sessions.
# Tips can be entered against historical games to see how well people perform in tipping against games
# that have already occurred. It is also intended to create a computer tipper, which will tip on various
# programmed criteria like win/loss record in previous games, position in league table and home and away
# win/loss record.

# Press Shift+F10 to execute this script. It has been updated to import files with Class definitions.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# The following line imports all class definitions from the FootballSeason.py, FootballComp.py etc
# files that hold classes
# CLICK ON .... IF THEY ARE NOT DISPLAYED

from FootballSeason import *
from FootballComp import *
from FootballTeam import *
from FootballCompLadder import *
from FootballGame import *
from FootballCompDraw import *
from FootballTeamPlayer import *
from FootballTeamCoach import *
from TipperCompetition import *
from Tipper import *
from Tips import *
from TipperCompLadder import *

import csv

#def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the top gutter to run the script.

# Below are the functions called within main.py. These are mainly functions to display details stored in
# files and create associated objects.

# All files contain comma separated values and are loaded into Lists. The lists for
# seasons and competitions have central identifying information


def read_football_competitions(AllComps_read_football_competitions):
    # As with all other file reads in the system, the file data is read into a list data structure.
    # Actions against the object are handle by manipulating the list data. The entire list is then
    # written back to the file for permanent storage.

    csv_filename = './Data/FootballCompetitions.csv'  # the permanent data file of football competitions

    with open( csv_filename, encoding="locale") as f:
        reader = csv.reader( f )
        AllComps_read_football_competitions = list(reader)
        numberLines = len( AllComps_read_football_competitions )
        if (numberLines > 0):
            print( f"FILE FootballCompetitions.csv READ WITH VALUES RETRIEVED:" )
            for i in range( numberLines ):
                print(AllComps_read_football_competitions[i])

    # CHECK IF numberLines = 0 then add competition (DO SAME FOR SEASONS)
    if (numberLines == 0):
        print("File FootballCompetitions.csv is empty. Please add a record.")
        # Below here is a duplication of the code for competition_choice == '3' (add competition) in process_competition routine
        newCompetition = input( "Input new competition in comma separated values of  compID, seasonID, compName: " )
        compID, seasonID, compName = newCompetition.split( "," )
        # Now create object for the football competition
        thisFootballComp_process_competition_Object = FootballComp( compID, seasonID, compName )
        thisFootballComp_process_competition_Object.addCompetition( AllComps_read_football_competitions,
                                                                    thisFootballComp_process_competition_Object, compID,
                                                                    seasonID, compName )
        numberLines = len( AllComps_read_football_competitions )
        # Add an entry into the list of competitions and write to file
        AllComps_read_football_competitions = read_football_competitions( AllComps_read_football_competitions )
        AllComps_read_football_competitions.append( [compID, seasonID, compName] )
        thisFootballComp_process_competition_Object.writeCompToFile( AllComps_read_football_competitions )
        print( f" Competition {compID}, Season {seasonID}, compName {compName} added: \n" )
        display_football_competions( AllComps_read_football_competitions )

    return AllComps_read_football_competitions

def find_football_comp (AllComps_find_football_comp, UserRequestedCompID_find_football_comp):
# go through the list of competitions and when find required comp create an object for it
    Desired_comp = UserRequestedCompID_find_football_comp
    Desired_comp_found = False
    numberLines = len(AllComps_find_football_comp)
    for i in range(numberLines): # go through file list line by line
        Current_line = AllComps_find_football_comp[i]

        if [Current_line[0]] == Desired_comp:
            Desired_comp_found = True
            thisCompID = Current_line[0]
            thisSeasonID = Current_line[1]
            thisCompName = Current_line[2]
            thisFootballComp_Object = FootballComp(thisCompID, thisSeasonID, thisCompName)
            print( "Football Comp Object Created:" )
            print(f"CompID is {thisFootballComp_Object.FootballCompID}, SeasonID is {thisFootballComp_Object.FootballSeasonID}, CompName is {thisFootballComp_Object.FootballCompName}\n" )

    if not Desired_comp_found:
        print( f"Desired season {Desired_comp} not in file" )

    return thisFootballComp_Object

def display_football_competitions(AllComps_display_football_competitions):
    numberLines = len( AllComps_display_football_competitions )

    # Display all lines of file
    print("COMPETITIONS")
    print("----------")
    print( "[CompID, SeasonID, CompName]" )
    for i in range( numberLines ):
        print( AllComps_display_football_competitions[i] )

def read_football_seasons(AllSeasons_read_football_seasons):
    # As with all other file reads in the system, the file data is read into a list data structure.
    # Actions against the object are handle by manipulating the list data. The entrire list is then
    # written back to the file for permanent storage.

    # seasonYear, seasonCompID, seasonstartDate, seasonendDate, seasonnumberRounds, seasonnumberTeams
#    global GLOBAL_AllSeasons # only need to declare name as global, not type (list) as well
    csv_filename = './Data/FootballSeasons.csv'
    with open( csv_filename, encoding="locale") as f:
        reader = csv.reader( f )
        AllSeasons_read_football_seasons = list( reader )

    return AllSeasons_read_football_seasons

def display_football_seasons(AllSeasons_display_football_seasons):
#    global GLOBAL_AllSeasons
    numberLines = len(AllSeasons_display_football_seasons)
    print( "" )
    print( "FOOTBALL SEASONS" )
    print( "----------------" )
    print( "[SeasonID, SeasonYear, CompID, StartDate, EndDate, NumberOfGames, NumberOfTeams]" )
    for i in range( numberLines ):  # print each line
        print( AllSeasons_display_football_seasons[i] )

    return

def find_football_season(AllSeasons_find_football_season, FootballSeasonID_find_football_season):

    thisFootballSeason_find_football_season_Object=[]

    numberLines = len( AllSeasons_find_football_season )
    Desired_season = FootballSeasonID_find_football_season
    Desired_season_found = False
    for i in range( numberLines ):  # go through file list line by line
        Current_line = AllSeasons_find_football_season[i]
        if [Current_line[0]] == Desired_season:
            Desired_season_found = True
            occurrenceInAllSeasons = i
            # variables starting 'this' are attributes of user requested season
            thisseasonID = UserRequestedFootballSeasonID
            thiscompID = Current_line[1]
            thisstartDate = Current_line[2]
            thisendDate = Current_line[3]
            thisnumberRounds = Current_line[4]
            thisnumberTeams = Current_line[5]

            # Now create object for the football season
            thisFootballSeason_find_football_season_Object = FootballSeason( thisseasonID, thiscompID, thisstartDate, thisendDate, thisnumberRounds, thisnumberTeams)
            print( "Football Season Object Created:" )
            print(f"SeasonID is {thisFootballSeason_find_football_season_Object.SeasonID}, CompID is {thisFootballSeason_find_football_season_Object.SeasonFootballCompID}, startDate is {thisFootballSeason_find_football_season_Object.SeasonStartDate}, endDate is {thisFootballSeason_find_football_season_Object.SeasonEndDate}, numberGames is {thisFootballSeason_find_football_season_Object.SeasonNumberGames}, numberTeams is {thisFootballSeason_find_football_season_Object.SeasonNumberTeams}\n" )

    if not Desired_season_found:
        print(f"Desired season {Desired_season} not in file")

    return thisFootballSeason_find_football_season_Object

def read_teams(AllTeams_read_teams):
    # As with all other file reads in the system, the file data is read into a dictionary data structure.
    # Actions against the object are handled by manipulating the dictionary data. The entrire dictionary is then
    # written back to the file for permanent storage.

    file = './Data/FootballTeams.csv'  # the permanent data file of football teams

    with open( csv_filename, encoding="locale" ) as f:
        reader = csv.reader( f )

        AllTeams = list( reader )
    return AllTeams_read_teams

def display_teams(AllTeams_display_teams): # displaying an object involves displaying the appropriate dictionary

    numberLines = len( AllTeams )
    print( "" )
    print( "FOOTBALL TEAMS" )
    print( "----------------" )
    print( "[TeamID, SeasonID, CompID, TeamName]" )
    for i in range( numberLines ):  # print each line
        print( AllTeams[i] )

    return

# Within each of the process_<object> functions  display a submenu to provide options on actions to perform
# against each of the objects. This will then result in the calling of a function within each of the
# necessary classes

def process_season(AllSeasons_process_season, thisFootballSeason_process_season_Object):

    print("These are the current seasons:")
    AllSeasons_process_season = read_football_seasons(AllSeasons_process_season)
    display_football_seasons(AllSeasons_process_season)
    still_processing_season = True
    while still_processing_season:
        print( f"Select what to do to with a season:" )
        print( f"1. Display Existing Football Seasons" )
        print( f"2. Update a Football Season" )
        print( f"3. Add another Football Season" )
        print( f"4. Delete a Football Season" )
        print( "X or x. Exit" )

        season_choice = input( "Enter your choice (1-9 or X):" )

        if season_choice == 'X' or season_choice == 'x':
            print( "Bye until next time" )
            still_processing_season = False
        elif season_choice == '1': # Display existing seasons
            AllSeasons_process_season = read_football_seasons( AllSeasons_process_season )
            display_football_seasons( AllSeasons_process_season )
        elif season_choice == '2': # Update existing system
            display_football_seasons(AllSeasons_process_season)
            seasonToUpdate = input( "ID of season to update: " )
            # convert string input to list element
            seasonToUpdate = [seasonToUpdate]
            seasonID = seasonToUpdate
            compID = "Update the field to compID"
            compID = [compID]
            startDate = "Update the field to startDate"
            startDate = [startDate]
            endDate = "Update the field to endDate"
            endDate = [endDate]
            numberGames = "Update the field to numberGames"
            numberGames = [numberGames]
            numberTeams = "Update the field to numberTeams"
            numberTeams = [numberTeams]

            find_football_season(AllSeasons_process_season,seasonToUpdate)
            updatedSeason = input( "Enter new season as comma separated values seasonID,compID,startDate,endDate,numberGames,numberTeams: " )
            updatedSeason = updatedSeason.split( "," )
            # Update the list, write to file and recreate object
            numberLines = len( AllSeasons_process_season )
            Desired_season = seasonToUpdate
            Desired_season_found = False
            for i in range( numberLines ):  # go through file list line by line
                Current_line = AllSeasons_process_season[i]
                if [Current_line[0]] == Desired_season:
                    Desired_season_found = True
                    AllSeasons_process_season[i] = updatedSeason
                    thisFootballSeason_process_season_Object = FootballSeason( seasonID, compID, startDate, endDate,
                                                                       numberGames, numberTeams )
                    thisFootballSeason_process_season_Object.writeSeasonToFile( AllSeasons_process_season )
                    print( f"Season {seasonID}, Start {startDate}, End {endDate} updated: \n" )
                    break

            if not Desired_season_found:
                print(f"Season {Desired_season} not found")
            # Display all seasons, showing changed season or no change
            display_football_seasons( AllSeasons_process_season )

        elif season_choice == '3': # Add season
            newSeason=input("Input new season in comma separated values of seasonID, compID, startDate, endDate, numberGames, numberTeams: ")
            seasonID, compID, startDate, endDate, numberGames, numberTeams = newSeason.split( "," )
            # Now create object for the football season
            thisFootballSeason_process_season_Object = FootballSeason( seasonID, compID, startDate, endDate, numberGames, numberTeams )
            thisFootballSeason_process_season_Object.addSeason(AllSeasons_process_season, thisFootballSeason_process_season_Object,seasonID, compID, startDate, endDate, numberGames, numberTeams)
            numberLines = len( AllSeasons_process_season )
            # Add an entry into the list of seasons and write to file
            AllSeasons_process_season = read_football_seasons( AllSeasons_process_season )
            AllSeasons_process_season.append( [seasonID, compID, startDate, endDate, numberGames, numberTeams] )
            thisFootballSeason_process_season_Object.writeSeasonToFile(AllSeasons_process_season)
            print(f"Season {seasonID}, Start {startDate}, End {endDate} added: \n")
            display_football_seasons(AllSeasons_process_season)

        elif season_choice == '4': # Delete season
            #Request season to delete
            seasonToDelete = input( "ID of season to delete: " )
            # convert string input to list element
            seasonToDelete = [seasonToDelete]

            #Find season to delete in list
            numberLines = len(AllSeasons_process_season)
            Desired_season = seasonToDelete
            Desired_season_found = False
            for i in range( numberLines ):  # go through file list line by line
                Current_line = AllSeasons_process_season[i]
                if [Current_line[0]] == Desired_season:
                    Desired_season_found = True
                    Desired_season_index = i
                    thisFootballSeason_process_season_Object = FootballSeason( Current_line[0], Current_line[1], Current_line[2], Current_line[3],
                                                                               Current_line[4], Current_line[5] )
            if Desired_season_found:
                del AllSeasons_process_season[Desired_season_index]
            # Write list to disk
            thisFootballSeason_process_season_Object.writeSeasonToFile( AllSeasons_process_season )
            # Delete object with seasonID
            del thisFootballSeason_process_season_Object
            # Display all seasons, showing season has been deleted
            AllSeasons_process_season = read_football_seasons( AllSeasons_process_season )
            display_football_seasons( AllSeasons_process_season )
#    GLOBAL_thisFootballSeason.addTeam()
#    print(f"Team added {GLOBAL_thisFootballSeason.SeasonNumberTeams}")

    return

def process_competition(AllComps_process_competition, thisFootballComp_process_competition_Object):
    print("These are the current competitions:")
    AllComps_process_competition = read_football_competitions(AllComps_process_competition)
    display_football_competitions(AllComps_process_competition)
    still_processing_competition = True
    while still_processing_competition:
        print( f"Select what to do to with competition(s):" )
        print( f"1. Display Existing Football Competitions" )
        print( f"2. Update a Football Competition" )
        print( f"3. Add another Football Competition" )
        print( f"4. Delete a Football Competition" )
        print( "X or x. Exit" )

        competition_choice = input( "Enter your choice (1-9 or X):" )

        if competition_choice == 'X' or competition_choice == 'x':
            print( "Bye until next time" )
            still_processing_competition = False
        elif competition_choice == '1': # Display existing competitions
            AllComps_process_competition = read_football_competitions( AllComps_process_competition )
            display_football_competitions( AllComps_process_competition )
        elif competition_choice == '2': # Update existing competition
            display_football_competitions(AllComps_process_competition)
            competitionToUpdate = input( "ID of competition to update: " )
            # convert string input to list element
            competitionToUpdate = [competitionToUpdate]
            compID = competitionToUpdate
            seasonID = "Update the field to seasonID"
            seasonID = [seasonID]
            competitionName = "Update the field to competitionName"
            competitionName = [competitionName]
            find_football_comp(AllComps_process_competition,competitionToUpdate)
            updatedComp = input( "Enter new competition as comma separated values compID,seasonID,compName: " )
            updatedComp = updatedComp.split( "," )
            # Update the list, write to file and recreate object
            numberLines = len( AllComps_process_competition )
            Desired_competition = competitionToUpdate
            Desired_competition_found = False
            for i in range( numberLines ):  # go through file list line by line
                Current_line = AllComps_process_competition[i]
                if [Current_line[0]] == Desired_competition:
                    Desired_competition_found = True
                    AllComps_process_competition[i] = updatedComp
                    thisFootballComp_process_competition_Object = FootballComp( compID, seasonID,  competitionName )
                    thisFootballComp_process_competition_Object.writeCompetitionToFile( AllComps_process_competition )
                    print( f"Competition {compID}, Season {seasonID}, CompName {competitionName} updated: \n" )
                    break

            if not Desired_competition_found:
                print(f"Competition {Desired_competition} not found")
            # Display all competitions, showing changed competition or no change
            display_football_competitions( AllComps_process_competition )

        elif competition_choice == '3': # Add competition
            newCompetion=input("Input new competition in comma separated values of  compID, seasonID, compName: ")
            compID, seasonID, compName = newCompetion.split( "," )
            # Now create object for the football competition
            thisFootballComp_process_competition_Object = FootballComp( compID, seasonID, compName )
            thisFootballComp_process_competition_Object.addCompetition(AllComps_process_competition, thisFootballComp_process_competition_Object, compID, seasonID, compName)
            numberLines = len( AllComps_process_competition )
            # Add an entry into the list of competitions and write to file
            AllComps_process_competition = read_football_competitions( AllComps_process_competition )
            AllComps_process_competition.append( [compID, seasonID, compName] )
            thisFootballComp_process_competition_Object.writeCompetitionToFile(AllComps_process_competition)
            print(f" Competition {compID}, Season {seasonID}, compName {compName} added: \n")
            display_football_competitions(AllComps_process_competition)

        elif competition_choice == '4': # Delete competition
            #Request competition to delete
            competitionToDelete = input( "ID of competition to delete: " )
            # convert string input to list element
            competitionToDelete = [competitionToDelete]

            #Find season to delete in list
            numberLines = len(AllComps_process_competition)
            Desired_competition = competitionToDelete
            Desired_competition_found = False
            for i in range( numberLines ):  # go through file list line by line
                Current_line = AllComps_process_competition[i]
                if [Current_line[0]] == Desired_competition:
                    Desired_competition_found = True
                    Desired_competition_index = i
                    thisFootballComp_process_competition_Object = FootballComp( Current_line[0], Current_line[1], Current_line[2] )
            if Desired_competition_found:
                del AllComps_process_competition[Desired_competition_index]
            # Write list to disk
            thisFootballComp_process_competition_Object.writeCompetitionToFile( AllComps_process_competition )
            # Delete object with compID
            del thisFootballComp_process_competition_Object
            # Display all competitions, showing competition has been deleted
            AllComps_process_competition = read_football_competitions( AllComps_process_competition )
            display_football_competitions( AllComps_process_competition )

    return

def process_ladder():
    pass

    return

def process_draw():
    pass

    return

def process_team():
#    This function to be redeveloped using different approach - will use list of lists and not dictionaries

    still_processing_team = True

    while still_processing_team:
        print("Select what action to perform with a team:\n")
        print("1. Display Teams")
        print("2. Update Team")
        print("3. Add Team")
        print("4. Delete Team")
        print( "X. Exit" )

        team_choice = input("Enter your choice (1-4 or X): ")

        if team_choice == 'X' or team_choice == 'x':
            print( "Bye until next time" )
            still_processing_team = False
        elif team_choice == '1':
            teamID_Name_Dict = {}  # initialise and empty dictionary
            teamID_Name_Dict = read_teams(teamID_Name_Dict)
            display_teams(teamID_Name_Dict)
        elif team_choice == '2':
            display_teams()
            teamToUpdate = input("ID of team to update: ")
            thisFootballTeam = FootballTeam(compID, seasonID, teamID, teamName)
            print("Comp ID = {compID}")
            print( "Season ID = {seasonID}")
            print( "Team ID = {teamID}")
            print( "Team Name = {teamName}")
            newName = input( "Enter new Team Name: " )

            thisFootballTeam.update_football_team()
        elif team_choice == '3':
            pass
#            display_teams()
#            teamToAdd = input( "Name of team to add: ")
# Work out ID of team (next unique number)
#            add_football_team()
        elif team_choice == '4':
            pass


    return

def process_result():
    pass

    return

def process_tippers():
    pass

    return

def process_tips():
    pass

    return

def process_tipper_competition():
    pass

    return

# It is a widely accepted habit to have the main starting code in a main() function. This is because it is
# a standard thing to do in other languages like C++ and java

def main():

#    AllSeasons=[]
#    thisFootballSeason_Object=[]

# Once the season and competition have been specified, present a menu to establish which object is to be
# processed - all are linked to specific seasons and competitions.

    is_running = True

    while is_running:
        print("Select what to process:\n")
        print("1. Football Season")
        print("2. Football Competition")
        print("3. Football Ladder")
        print("4. Football Competition Draw")
        print("5. Football Team")
        print("6. Football Game and Result")
        print("7. Tippers")
        print("8. Tips")
        print("9. Tipper Competition Ladder")
        print("X. Exit")

        choice = input("Enter your choice (1-9 or X):")

        if choice == 'X' or choice == 'x':
            print( "Bye until next time" )
            is_running = False
        elif choice == '1':
            process_season(AllSeasons, thisFootballSeason_Object)
        elif choice == '2':
            process_competition(AllComps, thisFootballComp_Object)
        elif choice == '3':
            process_ladder()
        elif choice == '4':
            process_draw()
        elif choice == '5':
            process_team()
        elif choice == '6':
            process_result()
        elif choice == '7':
            process_tippers()
        elif choice == '8':
            process_tips()
        elif choice == '9':
            process_tipper_competition()
        else:
            print( f"{choice} is not a valid choice" )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# The following check of __name__ is a standard Python check to make sure that the program is being
# deliberately run (when __name__ == '__main__'), rather than run when code imported

if __name__ == '__main__':
    # Gain user input to find out what football code and football season are to be processed
    # This will be later developed into a fancy web page input
    AllSeasons=[]
    AllSeasons = read_football_seasons(AllSeasons)
    display_football_seasons(AllSeasons)
    UserRequestedFootballSeasonID = input("Enter football season ID of competition (Currently only '02', which is '2025' has associated data): ")
    UserRequestedFootballSeasonID = [UserRequestedFootballSeasonID]
    thisFootballSeason_Object = find_football_season(AllSeasons, UserRequestedFootballSeasonID)

    AllComps=[]
    AllComps = read_football_competitions(AllComps)
    display_football_competitions(AllComps)
    UserRequestedCompID = input("ID of football competition (Currently only 'EPL (01)' has linked data): ")
    UserRequestedCompID = [UserRequestedCompID]
    thisFootballComp_Object = find_football_comp(AllComps, UserRequestedCompID)

    # Best way to enter tips and results will probably be to enter these into csv files.
    # In real life people would email, telephone or otherwise get tips to you, and you would update the necessary
    # csv file(s). Similarly, after games are played you would update csv file(s) with the results.
    # Could later develop fancy web interface for editing the csv files

# After global objects and lists for season and competition created - can call main() function and present menus

main()

