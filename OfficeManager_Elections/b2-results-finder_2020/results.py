import csv

#######################################################################################
# IMPORTANT: before reusing this program, make sure these constants are set correctly #
#######################################################################################
NUM_ROWS_TO_SKIP = 3 # number of csv rows (not file lines) of the file that are metadata. needs to be the same for both files
EMAIL_COL = 11 # needs to be the same for both files
FIRST_YEAR_CSV_FILENAME = "Block+2+2020+First-Year+Ballot_October+2%2C+2020_12.10.csv"
SOPH_JUN_SEN_CSV_FILENAME = "Block+2+2020+Sophomore%2FJunior%2FSenior+Ballot_October+2%2C+2020_12.11.csv"
FIRST_YEAR_COLS = { # maps position names to a list of the column indices in the first-year csv file that represent votes for that position
    "First-Year Rep": [17,18,19],
    "Inclusion Officer": [20],
    "Finance Rep": [21]
}
SOPH_JUN_SEN_COLS = { # maps position names to a list of the column indices in the sophomore/junior/senior csv file that represent votes for that position
    "Inclusion Officer": [17],
    "Finance Rep": [18]
}
ALL_FILENAMES_AND_COL_DICTS = [ # the variable through which the program loops in order to record all votes
    (FIRST_YEAR_CSV_FILENAME, FIRST_YEAR_COLS),
    (SOPH_JUN_SEN_CSV_FILENAME, SOPH_JUN_SEN_COLS)
]
#######################################################################################


# list of all voter emails, so that we notice if an email has multiple ballots submitted
voter_emails = []

# the dictionary that will map each position name to a dictionary of votes (inner dictionaries will map candidate name to their vote count)
all_votes = dict()


def record_votes_from_file(filename, file_cols: dict):
    """Record the votes in the specified CSV file, using the parameter file_cols as an indicator of which CSV columns correspond to votes for which position."""
    
    with open(filename, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_index = 0
        prev_row_len = 0
        for row in csv_reader:
            
            # report if this row contains a different number of columns from the previous row
            if len(row) != prev_row_len and row_index != 0:
                print(f"Warning on row #{row_index} (counting from 0) of {filename}: current row has a different number of columns (commas) from the previous row")
                print(row)
                print("")
            
            # update previous row length tracker
            prev_row_len = len(row)

            # skip file metadata rows
            if row_index < NUM_ROWS_TO_SKIP:
                row_index += 1
                continue

            # report any weirdness relating to the email address in this row
            email = row[EMAIL_COL]
            if email in voter_emails:
                print(f"Warning on row #{row_index} (counting from 0) of {filename}: recording a ballot from {email}, who has already had a ballot previously recorded")
                print("")
            if email == "":
                print(f"Warning on row #{row_index} (counting from 0) of {filename}: recording a ballot without an associated email address")
                print(row)
                print("")
            else:
                if email[-20:] != "@coloradocollege.edu":
                    print(f"Warning on row #{row_index} (counting from 0) of {filename}: recording a ballot from a non-CC email address ({email})")
                    print("")
                
                # note that a ballot has been recorded from this email address, given that there is one for this ballot
                voter_emails.append(email)
            
            # record the votes from this ballot, for each position
            for position_name, position_cols in file_cols.items():
                for col in position_cols:
                    
                    candidate_name = row[col]

                    # ignore unused votes
                    if candidate_name == "":
                        continue
                    
                    # make sure candidate is in the votes dictionary for this position
                    # if so, increment their vote total
                    # if not, add them to the dictionary with a vote count of 1
                    if candidate_name in all_votes[position_name]:
                        all_votes[position_name][candidate_name] += 1
                    else:
                        all_votes[position_name][candidate_name] = 1

            # update row counter
            row_index += 1


def main():
    
    print("")

    # Step 1: loop through each (filename, columns-dictionary) pair to record votes
    for filename, file_cols in ALL_FILENAMES_AND_COL_DICTS:
        
        # make sure each position on this ballot type is in the votes dictionary
        for position_name in file_cols:
            if position_name not in all_votes:
                all_votes[position_name] = dict()
        
        # record the votes from this file
        record_votes_from_file(filename, file_cols)
    
    # Step 2: loop through the votes dictionary to sort and print results for each position
    print("\n --------- \n| RESULTS |\n --------- \n")
    for position_name, position_votes in all_votes.items():
        
        # sort the candidates from most to least votes
        sorted_position_votes = sorted(position_votes.items(), key=lambda candidate: candidate[1], reverse=True)

        # print the results for this position
        print("")
        print(position_name)
        for name, count in sorted_position_votes:
            print(f"{name}: {count}")
        
    print("")


if __name__ == "__main__":
    main()
