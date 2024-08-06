import csv
from ranked_ballot import RankedBallot

#######################################################################################
# IMPORTANT: before reusing this program, make sure these constants are set correctly #
#######################################################################################
QUESTION_TEXT_ROW = 1 # the csv row (not file line) of the file that contains metadata including question text. Used for parsing candidate names for ranked choice voting. Needs to be the same for all files
NUM_ROWS_TO_SKIP = 3 # number of csv rows (not file lines) of the file that are metadata. Needs to be the same for all files
EMAIL_COL = 11 # needs to be the same for all files

CSV_FILENAME = "Block+6+2021+Student+Trustee+and+Executive+Council+Ballot_March+19%2C+2021_12.13.csv"
SIMPLE_VOTE_COLS = { # maps position names to a list of the column indices (0-indexed) in the csv file that represent normal votes for that position
    "Student Trustee": [17],
    "President": [18],
    "VP of Inclusion": [19],
    "VP of Finance": [20]
}
RANKED_VOTE_COLS = { # maps position names to a list of the column indices (0-indexed) in the csv file that represent ranked votes for that position
    "VP of Outreach": [21,22,23,24]
}
# can add more such filenames and cols dicts for other files. Just make sure to add them to ALL_FILENAMES_AND_COL_DICTS below

ALL_FILENAMES_AND_COL_DICTS = [ # the variable through which the program loops in order to record the votes from all files. List of (filename, simple_vote_cols, ranked_vote_cols) tuples — one tuple per file
    (CSV_FILENAME, SIMPLE_VOTE_COLS, RANKED_VOTE_COLS)
]
################################################################
# The code below this point shouldn't normally have to change. #
################################################################

# list of all voter emails, so that we notice if an email has multiple ballots submitted
voter_emails = []

# the dictionaries that will map each position name to its vote distribution
# for simple votes, each dict entry will be an inner dictionary that will map candidate name to their vote count
# for ranked votes, each dict entry will be an inner dictionary that will map candidate name to a list of the RankedBallots that prefer them
all_simple_votes = dict()
all_ranked_votes = dict()

def record_votes_from_file(filename, simple_vote_cols: dict, ranked_vote_cols: dict):
    """Record the votes in the specified CSV file, using the simple_vote_cols and ranked_vote_cols parameters as indicators of which CSV columns correspond to votes for which position."""
    
    with open(filename, newline='') as csv_file:
        
        # a dictionary that maps ranked-vote position names to ordered lists of candidate names for those positions. The order is simply the order they're encountererd in the file, but it's important to preserve this order as long as we're dealing with this file
        ranked_candidate_names = dict()
        
        # more pre-loop setup
        csv_reader = csv.reader(csv_file)
        row_index = 0
        prev_row_len = 0

        for row in csv_reader:
            
            # report if this row contains a different number of columns from the previous row
            if len(row) != prev_row_len and row_index != 0:
                print(f"Warning on row {row_index + 1} of {filename}: current row has a different number of columns (commas) from the previous row")
                print(row)
                print("")
            
            # update previous row length tracker
            prev_row_len = len(row)

            # check if row contains question text metadata
            if row_index == QUESTION_TEXT_ROW:
                
                # for each position up for ranked-vote election:
                for position_name, position_cols in ranked_vote_cols.items():

                    # create a list to store the candidate names for this position
                    position_candidate_names = []

                    # for each candidate in this election:
                    for col in position_cols:
                        
                        # parse the question text metadata for the candidate name
                        question_text = row[col]
                        for j in range(len(question_text) - 1, 0, -1):
                            if question_text[j-2:j+1] == ' - ':
                                # add the candidate name to this position's ordered list of candidate names
                                candidate_name = question_text[j+1:]
                                position_candidate_names.append(candidate_name)

                    # add this position's candidate-names list to the ranked_candidate_names dictionary
                    ranked_candidate_names[position_name] = position_candidate_names


            # now, skip file metadata rows
            if row_index < NUM_ROWS_TO_SKIP:
                row_index += 1
                continue

            # report any weirdness relating to the email address in this row
            email = row[EMAIL_COL]
            if email in voter_emails:
                print(f"Warning on row {row_index + 1} of {filename}: recording a ballot from {email}, who has already had a ballot previously recorded")
                print("")
            if email == "":
                print(f"Warning on row {row_index + 1} of {filename}: recording a ballot without an associated email address")
                print(row)
                print("")
            else:
                if email[-20:].lower() != "@coloradocollege.edu":
                    print(f"Warning on row {row_index + 1} of {filename}: recording a ballot from a non-CC email address ({email})")
                    print("")
                
                # note that a ballot has been recorded from this email address, given that there is one for this ballot
                voter_emails.append(email)
            
            # record the simple votes from this ballot, for each simple-vote position
            for position_name, position_cols in simple_vote_cols.items():
                for col in position_cols:
                    
                    candidate_name = row[col]

                    # ignore unused votes
                    if candidate_name == "":
                        continue
                    
                    # make sure candidate is in the votes dictionary for this position
                    # if so, increment their vote total
                    # if not, add them to the dictionary with a vote count of 1
                    if candidate_name in all_simple_votes[position_name]:
                        all_simple_votes[position_name][candidate_name] += 1
                    else:
                        all_simple_votes[position_name][candidate_name] = 1
            
            # record the ranked votes from this ballot, for each ranked-vote position
            for position_name, position_cols in ranked_vote_cols.items():
                
                # create a ballot for the voter's choices for this position
                ballot = RankedBallot()
                
                # for each candidate up for this position:
                for candidate_index in range(len(position_cols)):
                    
                    col = position_cols[candidate_index] # the file column corresponding to this candidate
                    rank = row[col] # this voter's rank for this candidate

                    # ignore candidates this voter didn't rank
                    if rank == "":
                        continue
                    
                    # add this candidate ranking to the voter's ballot for this position
                    ballot.add_vote(candidate_name=ranked_candidate_names[position_name][candidate_index], rank=int(rank))
                
                # if the ballot isn't empty, add it to the list of votes for its top-ranked voter (making sure that list exists)
                if not ballot.is_empty():
                    top_candidate_name = ballot.get_top_candidate_name()
                    if top_candidate_name in all_ranked_votes[position_name]:
                        all_ranked_votes[position_name][top_candidate_name].append(ballot)
                    else:
                        all_ranked_votes[position_name][top_candidate_name] = [ballot]


            # update row counter
            row_index += 1
        
        # for clarity, make sure each ranked-voting candidate is included in the results, even if they didn't get any votes
        for position_name, candidate_names in ranked_candidate_names.items():
            for candidate_name in candidate_names:
                if candidate_name not in all_ranked_votes[position_name]:
                    all_ranked_votes[position_name][candidate_name] = []
        

def main():
    
    print("")

    # Step 1: loop through each (filename, columns-dictionary) pair to record votes
    for filename, simple_vote_cols, ranked_vote_cols in ALL_FILENAMES_AND_COL_DICTS:
        
        # make sure each position from this file's ballots is in the appropriate votes dictionary
        for position_name in simple_vote_cols:
            if position_name not in all_simple_votes:
                all_simple_votes[position_name] = dict()
        for position_name in ranked_vote_cols:
            if position_name not in all_ranked_votes:
                all_ranked_votes[position_name] = dict()
        
        # record the votes from this file
        record_votes_from_file(filename, simple_vote_cols, ranked_vote_cols)

    # Step 2: loop through the simple votes dictionary to sort and print results for each simple-vote position
    print("\n --------- \n| RESULTS |\n --------- \n")
    for position_name, position_votes in all_simple_votes.items():
        
        # sort the candidates from most to least votes
        sorted_position_votes = sorted(position_votes.items(), key=lambda candidate: candidate[1], reverse=True)

        # print the results for this position
        total_votes = sum(votes for name, votes in sorted_position_votes)
        print("")
        print(position_name)
        for name, count in sorted_position_votes:
            print(f"{name}: {count} ({round(100*count/total_votes, 2)}%)")
        
    print("")

    # Step 3: process the ranked-vote results, and output updates along the way
    for position_name, position_votes in all_ranked_votes.items():
        
        round_counter = 1
        
        while True:
            
            print(f"{position_name}, Round {round_counter}")
            
            # make sure there are still candidates in the running (could happen if the remaining two candidates tie)
            if len(position_votes) == 0:
                print("No candidates remaining")
                break

            # sort the candidates from most to least ballots favoring them
            sorted_position_votes = sorted(position_votes.items(), key=lambda candidate: len(candidate[1]), reverse=True)
            
            # count each candidate's ballots, and sum up the total number of active ballots
            vote_counts = [len(candidate_votes) for candidate_name, candidate_votes in sorted_position_votes] # this is sorted from most to least, which will be important
            total_vote_count = sum(vote_counts)

            # print some info
            for i in range(len(sorted_position_votes)):
                candidate_name = sorted_position_votes[i][0]
                candidate_count = vote_counts[i]
                print(f"{candidate_name}: {candidate_count} ({round(100*candidate_count/total_vote_count, 2)}%)")

            # see if the leader holds more than 50%
            if vote_counts[0] > total_vote_count / 2:
                print(f"\n{sorted_position_votes[0][0]} wins!")
                break

            # redistribute votes from the least popular candidate (or candidates, if there's a tie for least popular)
            i = len(vote_counts) - 1
            while i >= 0 and vote_counts[i] == vote_counts[-1]:
                losing_candidate_name = sorted_position_votes[i][0]
                for ballot in position_votes[losing_candidate_name]:
                    
                    ballot.remove_top_candidate()
                    
                    # skip over any next-preferred choices who have already been eliminated
                    while not ballot.is_empty() and ballot.get_top_candidate_name() not in position_votes:
                        ballot.remove_top_candidate()
                    
                    if not ballot.is_empty():
                        position_votes[ballot.get_top_candidate_name()].append(ballot)
                
                del position_votes[losing_candidate_name]
                i -= 1

            round_counter += 1
            print("")
        
        print("")


if __name__ == "__main__":
    main()
