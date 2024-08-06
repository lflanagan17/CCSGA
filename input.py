
#   Dictionary which holds all election data   # 
#   Only this information needs to be changed! # 




ELECTION_DATA = { 
    # Total number of students who were sent a ballot
    "Student total" : 2335, 
    #  row on the spreadsheet where the questions given (use actual row numbers on spreadsheet)
    "Question text row" : 2,
    # number of rows to skip on spreadsheet before you get to election data (or the spreadsheet row of the first data entry -1)
    # usually starts with something like "ImportId" #
    "Number of Rows to Skip" : 3, 
    # file name of the CSV file in the data folder
    "CSV file name" : "BLOCK_6_RESULTS.csv", 
    # the alphabetic letter of the column 
    "Email column" : "L", 
    # How many different elections are being run 
    "Number of Elections": 4, 
    # Election specific information 
    "Elections" : [
       { 
        # the name of the election (HOW IT APPEARS IN ROW 2)
        "Name" : "Q1", 
        # the columns on the spread sheet for that election 
        "Columns" : "R",  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "SIMPLE VOTE"
       },
       { 
        # the name of the election (HOW IT APPEARS IN ROW 2)
        "Name" : "Q2", 
        # the columns on the spread sheet for that election 
        "Columns" : "S",  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "SIMPLE VOTE"
       },
       { 
        # the name of the election (HOW IT APPEARS IN ROW 2)
        "Name" : "Q3", 
        # the columns on the spread sheet for that election 
        "Columns" : "T",  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "SIMPLE VOTE"
       },
       { 
        # the name of the election (HOW IT APPEARS IN ROW 2)
        "Name" : "Q4", 
        # the columns on the spread sheet for that election 
        "Columns" : "U",  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "SIMPLE VOTE"
       }
    ], 
    # if you want to not count completed ballots 
    "Count Incomplete Ballots": True, 
    # email address requirements -- (i.e. only .edu addresses or only schoolname.edu addresses)
    "Email Requirements": "@coloradocollege.edu", 
    # count invalid emails (false if you dont want to count invalid emails )
    "Invalid Emails": True, 
    # discard repeat votes (true if you dont want to count votes from the same email address)
    "Discard Repeats": False


} 

FILE_NAME = ""
ELECTIONS = []

NUM_ROWS_TO_SKIP = ELECTION_DATA["Number of Rows to Skip"]
EMAIL_COLUMN = ELECTION_DATA["Email column"]

EMAIL_REQUIREMENT = ELECTION_DATA["Email Requirements"]
DISCARD_REPEATS= ELECTION_DATA["Discard Repeats"]
INVALID_EMAILS = ELECTION_DATA["Invalid Emails"]
STUDENT_TOTAL = ELECTION_DATA["Student total"]
