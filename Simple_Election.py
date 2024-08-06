from tkinter import Place
from Election import Election 
class Simple_Election(Election): 
    def __init__(self, NAME_OF_ELECTION, COLUMNS, NUM_OF_SEATS_OPEN=1):
        self.NAME_OF_ELECTION = NAME_OF_ELECTION
        self.COLUMN = COLUMNS
        self.CANIDATE_VOTES = {}
        self.CANIDATE_NAMES = []
        self.RESULTS = {}
        self.TOTAL_VOTES = 0

        
    def record_data(self, data_row):
      
       # If the election is a SIMPLE VOTE 
        # Get the canidate vote -- COLUMNS for a simple vote should be a singular number
        canidate_vote = data_row[self.COLUMN]
        # Check if the canidate_vote (should be canidates name) is not already listed in canidate names
        if  canidate_vote != "": 
            if canidate_vote not in self.CANIDATE_NAMES: 
             # If not, add it and add 
                self.CANIDATE_NAMES.append(canidate_vote)
                self.CANIDATE_VOTES[canidate_vote] = 0
                self.RESULTS[len(self.CANIDATE_NAMES)] = ()
            self.TOTAL_VOTES += 1
            self.CANIDATE_VOTES[canidate_vote] += 1
       
    # Method to run elections for a simple election 
    def run_election(self):
        # for each canidate 
        i = 1
        for canidate, votes in sorted(self.CANIDATE_VOTES.items(), key = lambda votes: votes[1], reverse=True): 
            self.RESULTS[i] = (canidate, votes)
            i +=1 
        return self.RESULTS
    def print_results(self): 
        print(f"+++++++++++++++++++ RESULTS FOR {self.NAME_OF_ELECTION}++++++++++++++++")
        for place, (canidate, votes) in self.RESULTS.items(): 
            print( f"({place}) -- {canidate}-- {votes}\n")


    def get_results(self):
        return super().get_results()
    def get_name_of_election(self):
        return super().get_name_of_election()
    def get_number_of_votes(self):
        return super().get_number_of_votes()
    def get_canidate_names(self):
        return super().get_canidate_names()
    def make_canidate_names_to_columns(self, text_question_row):
        return super().make_canidate_names_to_columns(text_question_row)


