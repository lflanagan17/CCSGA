import csv
from Ranked_Election import Ranked_Election
from Simple_Election import Simple_Election
import string
from input import ELECTION_DATA



EMAIL_REQUIREMENT = ELECTION_DATA["Email Requirements"]
DISCARD_REPEATS= ELECTION_DATA["Discard Repeats"]
INVALID_EMAILS = ELECTION_DATA["Invalid Emails"]
STUDENT_TOTAL = ELECTION_DATA["Student total"]

FILE_NAME = ""
ELECTIONS = [] 

TOTAL_VOTES = 0

VOTER_EMAILS = [] 


# method to make the actual elections 
def make_elections():
   
    # Parse through election information
    for election in ELECTION_DATA["Elections"]: 
        # For each election being held, create an Election object
        elect = None
        type_of_election = election["Type of Election"]
        if type_of_election == "SIMPLE VOTE": 
            elect = Simple_Election( NAME_OF_ELECTION= election["Name"], COLUMNS = char_position(election["Columns"]), NUM_OF_SEATS_OPEN = 1)
        elif type_of_election == "RANKED CHOICE": 
            elect = Ranked_Election( NAME_OF_ELECTION= election["Name"], COLUMNS = char_position_maker(election["Columns"]), NUM_OF_SEATS_OPEN = election["Number of Seats"])
        # add elections to the list of elections 
        ELECTIONS.append(elect)
# Helper method to take a list of columns in alphabets and make them integers
def char_position_maker(columns): 
    c = []
    for letter in columns: 
        c.append(int(char_position(letter)))
    return c
# Helper method to take a singular alphabet letter and output its appropriate column number
def char_position(letter):
    if len(letter) == 1: 
        return string.ascii_lowercase.index(letter.lower())
    else: 
        v = 0
        for l in letter[:-1]: 
            v = v + char_position(l) + 1  * 25
        v += char_position(letter[-1])   
        return v
# code to run each election in ELECTIONS using the .run_election() in the Election interface 
def run_elections(): 
    print("============================= RUNNING ELECTIONS =============================")
    print("")
    for election in ELECTIONS: 
        print(f"============================= ELECTION: {election.NAME_OF_ELECTION} =============================")
        print("")

        election.run_election()
    print("=================================================================================")
    print("")
# print all election results syncronichasly 
def print_results(): 
    print("")
    print("################################## RESULTS ############################################")
    print("")
    for election in ELECTIONS: 
        print("")
        print(f"============================= {election.NAME_OF_ELECTION} ===============================") 
        election.print_results()
        print(f"=========================================================================================")
        print("")
    print("") 
    print(f"TURN OUT RATE: {int(TOTAL_VOTES/STUDENT_TOTAL*100)}%")
    print("\n")

# method to parse and record the data 
def record_data():
    TOTAL_VOTES= 0 
    # open file 
    with open(FILE_NAME, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_index = 0
        prev_row_len = 0
        text_question_row =""
        print("\n============================= RECORDING DATA ===========================")
        print("")
        # parse through the file
        for row in csv_reader:
            # if this is the question row,
            if row_index == QUESTION_TEXT_ROW: 
                text_question_row = row
                #  save the questions to the election 
                for election in ELECTIONS: 
                    #(this is only applicable for ranked choice but can be done for a simple election as well)
                    election.make_canidate_names_to_columns( text_question_row)


            
            # report if this row contains a different number of columns from the previous row
            if len(row) != prev_row_len and row_index != 0:
                print(f"Warning on row {row_index + 1} of {FILE_NAME}: current row has a different number of columns (commas) from the previous row")
                print("")
            
            # update previous row length tracker
            prev_row_len = len(row)

           


            # if this is before the start of election data, skip file metadata rows 
            if row_index < NUM_ROWS_TO_SKIP:
                row_index += 1
                continue
            # once we have reacheed the election data--- parse the election data to verify accetabke acount. 
            # if the email is verified and the entry is accepted, it will return true 
            if parse_emails_and_verify(row, row_index) == True: 
                # record that data for each election 
                TOTAL_VOTES = TOTAL_VOTES +  1 

                for election in ELECTIONS: 
                    election.record_data(row)
        print("")
        print("")
    print('TOTAL VOTES: ' + str(TOTAL_VOTES))
    return TOTAL_VOTES
def parse_emails_and_verify(row, row_index): 
    # report any weirdness relating to the email address in this row
        email = row[EMAIL_COLUMN]
        if email in VOTER_EMAILS:
            print(f"Warning on row {row_index + 1} of {FILE_NAME}: encountered a ballot from {email}, who has already had a ballot previously recorded")
            if DISCARD_REPEATS == True: 
                print("---not recorded")
                print("")

                return False
            print("---recorded") 
            print("")

        if email == "":
            print(f"Warning on row {row_index + 1} of {FILE_NAME}: encountered a ballot without an associated email address")
            if INVALID_EMAILS == False: 
                print("---not recorded")
                print("")

                return False
            print("---recorded")
            print("")
        else:
            if email[-len(EMAIL_REQUIREMENT):].lower() != EMAIL_REQUIREMENT:
                print(f"Warning on row {row_index + 1} of {FILE_NAME}: encountered a ballot from a non-CC email address ({email})")
                if INVALID_EMAILS == False: 
                    print("---not recorded")
                    print("")

                    return False
                print("---recorded")
                print("")

            
            # note that a ballot has been recorded from this email address, given that there is one for this ballot
            VOTER_EMAILS.append(email)
            return True
    
FILE_NAME = "data/"+ ELECTION_DATA["CSV file name"]
ELECTIONS = []
NUM_ROWS_TO_SKIP = ELECTION_DATA["Number of Rows to Skip"]
EMAIL_COLUMN = char_position(ELECTION_DATA["Email column"])
QUESTION_TEXT_ROW = ELECTION_DATA["Question text row"] - 1
TOTAL_VOTES = 0 

VOTER_EMAILS = [] 

make_elections()
TOTAL_VOTES = record_data()
run_elections()
print_results()





