# this is an example of what input.py should look like pulled from a previous election # 
# DOES NOT ADD ANY FUNCTIONALITY TO THE ELECTIONS PROGRAM # 


BLOCK_2_2021_FRESH_REP_ELECTION_DATA = { 
    "Student total" : 2500, 
    #  row on the spreadsheet where the questions given (use actual row numbers on spreadsheet)
    "Question text row" : 2,
    # number of rows to skip on spreadsheet before you get to election data (or the spreadsheet row of the first data entry -1)
    "Number of Rows to Skip" : 3, 
    # file name of the CSV file in the data folder
    "CSV file name" : "Block+2+2021+First-Year+Ballot+-_October+14%2C+2021_15.01.csv", 
    # the alphabetic letter of the column 
    "Email column" : "L", 
    # How many different elections are being run 
    "Number of Elections": 1, 
    # Election specific information 
    "Elections" : [
      
      
       { 
        # the name of the election 
        "Name" : "First Year Elections", 
        # the columns on the spread sheet for that election 
        "Columns" : ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD"],  
        # number of open seats 
        "Number of Seats" :5, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "RANKED CHOICE"
       } 


    ], 
    # if you want to not count completed ballots (NOT YET IMPLEMENTED )
    "Count Incomplete Ballots": True, 
    # email address requirements -- (i.e. only .edu addresses or only schoolname.edu addresses)
    "Email Requirements": "@coloradocollege.edu", 
    # count invalid emails (false if you dont want to count invalid emails )
    "Invalid Emails": False, 
    # discard repeat votes (true if you dont want to count votes from the same email address)
    "Discard Repeats": True


} 
BLOCK_6_2021_EXEC_ELECTION_DATA = { 
    # Total number of students at the school 
    "Student total" : 2500, 
    #  row on the spreadsheet where the questions given (use actual row numbers on spreadsheet)
    "Question text row" : 2,
    # number of rows to skip on spreadsheet before you get to election data (or the spreadsheet row of the first data entry -1)
    "Number of Rows to Skip" : 3, 
    # file name of the CSV file in the data folder
    "CSV file name" : "Block 6 2021 Student Trustee and Executive Council Ballot_February 28, 2022_14.38.csv", 
    # the alphabetic letter of the column 
    "Email column" : "L", 
    # How many different elections are being run 
    "Number of Elections": 3, 
    # Election specific information 
    "Elections" : [
      
       { 
        # the name of the election 
        "Name" : "Student Trustee", 
        # the columns on the spread sheet for that election 
        "Columns" : "R",  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- either RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "SIMPLE VOTE"
       },  
        { 
        # the name of the election 
        "Name" : "Student Body President", 
        # the columns on the spread sheet for that election 
        "Columns" : "S",  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "SIMPLE VOTE"
       } , 
       { 
        # the name of the election 
        "Name" : "VP Inclusion", 
        # the columns on the spread sheet for that election 
        "Columns" : "T",  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "SIMPLE VOTE"
       } , 
       { 
        # the name of the election 
        "Name" : "VP Finance", 
        # the columns on the spread sheet for that election 
        "Columns" : "U",  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "SIMPLE VOTE"
       } , 
       { 
        # the name of the election 
        "Name" : "VP of outreach", 
        # the columns on the spread sheet for that election 
        "Columns" : ["V", "W", "X", "Y"],  
        # number of open seats 
        "Number of Seats" :1, 
        # type of election -- eith RANKED CHOICE or SIMPLE VOTE
        "Type of Election" : "RANKED CHOICE"
       } 


    ], 
    # if you want to not count completed ballots (NOT YET IMPLEMENTED )
    "Count Incomplete Ballots": True, 
    # email address requirements -- (i.e. only .edu addresses or only schoolname.edu addresses)
    "Email Requirements": "@coloradocollege.edu", 
    # count invalid emails (false if you dont want to count invalid emails )
    "Invalid Emails": False, 
    # discard repeat votes (true if you dont want to count votes from the same email address)
    "Discard Repeats": True


} 
FILE_NAME = ""
ELECTIONS = []

NUM_ROWS_TO_SKIP = ELECTION_DATA["Number of Rows to Skip"]
EMAIL_COLUMN = ELECTION_DATA["Email column"]

EMAIL_REQUIREMENT = ELECTION_DATA["Email Requirements"]
DISCARD_REPEATS= ELECTION_DATA["Discard Repeats"]
INVALID_EMAILS = ELECTION_DATA["Invalid Emails"]
