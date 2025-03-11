# This is the hub Python script of the football tipping system. WITH CHANGES TO TEST COMMIT AND PUSH

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


# The following line import all class definitions from the FootballSeason.py and FootballComp.py files
from FootballSeason import *
from FootballComp import *

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the top gutter to run the script.
# The following check of __name__ is a standard Python check to make sure that the program is being
# deliberately run (when __name__ == '__main__'), rather than run when code imported

if __name__ == '__main__':

# Gain user input to find out what football code and football season are to be processed
# This will be later developed into a fancy web page input

    UserRequestedFootballCode = input("Football code of competition (Currently only 'EPL'):")
    UserRequestedFootballSeason = input("Football season of competition (Currently only '2025')")

# Best way to enter tips and results will probably be to enter these into text files.
# In real life people would email, telephone or otherwise get tips to you, and you would update the necessary
# text file(s). Similarly, after games are played you would update a text file(s) with the results.
# Could later develop fancy web interface for editing the text files

# READ FootballComp AND FootballSeason INFO FROM FILES

# First read the Season information into a variable and then split into substrings with split()
# I decided to read all core information from files in the main module. Substrings available throughout
# system

    file = "./Data/FootballSeasons.txt"

# The most widely used way of opening files is with f = open("demofile.txt", "rt") - 'r' for read and 't'
# for text are the defaults so no real need for them. Could also open file for appending, writing or
# creating. Good practice to close files when finished with them with f.close(). An encoding="locale" is
# also recommended when opening files since you do not know what encoding will be used on a computer on
# which the python program and text files will be stored and run (many python programs will be run on web
# servers, and you do not know what encoding is used on the web servers). Encoding is name given to the
# way binary 0's and 1's are converted to readable text - it is not always the same on all computers. If
# encoding="locale" is omitted then an encoding known as UTF-8 will be used and that would be fine on
# Linux and Mac computers but would not be handled properly on Windows computers. Use of encoding="locale"
# is a complex story and the above account only touches on the many issues. Google search for details if
# interested.

#
# This method below of reading file means the file does not have to be explicitly closed.
# encoding="locale" included since message displayed without and may otherwise
# cause problems if run on Windows machine. Google search to find details.

    with open(file, "rt", encoding="locale") as f:
        data = f.read()

    separated = data.split(sep=", ")
    seasonID = separated[0]
    compID = separated[1]
    startDate = separated[2]
    endDate = separated[3]
    numberRounds = separated[4]
    numberTeams = separated[5]

# The below simple test would have to be developed into something more advanced so that only records
# for the requested season are read from the file. Currently on one record in text file
    if seasonID == UserRequestedFootballSeason:
        print("\n")
        print(f"FILE FootballSeasons.txt READ WITH VALUES RETRIEVED:")
        print(f"ID is {seasonID}, Comp is {compID}, Start Date is {startDate}, End Date is {endDate}, Number of Rounds is {startDate}, Number of Teams is {numberTeams}")

# Now create object for the football season
        thisFootballSeason = FootballSeason(seasonID, compID, startDate, endDate, numberRounds, numberTeams)
        print("Football Season Object Created:")
        print(f"SeasonID is {thisFootballSeason.SeasonID}, CompID is {thisFootballSeason.SeasonFootballCompID}, startDate is {thisFootballSeason.SeasonStartDate}, endDate is {thisFootballSeason.SeasonEndDate}, numberGames is {thisFootballSeason.SeasonNumberGames}, numberTeams is {thisFootballSeason.SeasonNumberTeams}\n")

# After season information read, read information about competition in season
    file = './Data/FootballCompetitions.txt'
# See comment above about this method of reading file
    with open(file, "rt", encoding="locale") as f:
        data = f.read()

    separated = data.split(sep=", ")
    ID = separated[0]
    year = separated[1]
    code = separated[2]

# As for reading the seasons text file above, the below simple test would have to be developed so that only
# records for the requested season and football code are read from the file. Currently on one record in
# text file
    if year == UserRequestedFootballSeason and code == UserRequestedFootballCode:
        print(f"FILE FootballCompetitions.txt READ WITH VALUES RETRIEVED:")
        print(f"ID is {ID}, Year is {year}, Code is {code}\n")

#  Now create object for the football competition
        thisFootballComp = FootballComp(ID, year, code)
        print("Football Competition Object Created:")
        print(f"ID is {thisFootballComp.FootballCompID}, Season is {thisFootballComp.FootballSeasonID}, Code is {thisFootballComp.FootballCode}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
