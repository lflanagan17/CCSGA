import RankedBallot
from abc import ABC, abstractmethod
# Interface for elections


class Election(ABC): 
    # NAME_OF_ELECTION  a string representing the name of the election running
    # COLUMNS a list or single number specifying which column the question isasked 
    #  NUM_OF_SEATS_OPEN integer used to specify how manypositions are open -- RANKED CHOICE ONLY 
    def __init__(self, NAME_OF_ELECTION, COLUMNS, NUM_OF_SEATS_OPEN=1 ): 
        self.CANIDATE_NAMES = []
        self.NAME_OF_ELECTION = NAME_OF_ELECTION
        self.TOTAL_VOTES = 0 
        self.RESULTS = {}

        pass
    #METHOD TO RECORD DATA 
    @abstractmethod
    def record_data(self, data_row): 
       pass
    @abstractmethod
    def run_election(self): 
        pass
    # FOR RANKED CHOICE ONLY 
    @abstractmethod
    def print_results(self): 
        pass
    @abstractmethod
    def get_results(self): 
        return self.RESULTS
    @abstractmethod
    def get_number_of_votes(self):
        return self.TOTAL_VOTES 
    @abstractmethod
    def get_canidate_names(self): 
        return self.CANIDATE_NAMES
    @abstractmethod
    def get_name_of_election(self): 
        return self.NAME_OF_ELECTION
    @abstractmethod
    def make_canidate_names_to_columns(self, text_question_row): 
         pass
  

