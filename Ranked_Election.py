from math import ceil
from RankedBallot import RankedBallot
from Election import Election
DIVIDER = "++++++++++++++++"
class Ranked_Election(Election): 

    def __init__(self, NAME_OF_ELECTION, COLUMNS, NUM_OF_SEATS_OPEN=1 ): 
        # NAME OF THE ELECTION INPUT
        self.NAME_OF_ELECTION = NAME_OF_ELECTION
        # The columns with data in it 
        self.COLUMNS = COLUMNS
        # number of seats that are open 
        self.NUM_OF_SEATS_OPEN = NUM_OF_SEATS_OPEN
        self.CANIDATE_NAMES = []
        self.ELIMINATED = 0 
        self.TOP_CANIDATES_BALLOT = {}
        self.ALL_BALLOTS_FOR_CANIDATE = {}
        self.RESULTS = {}
        self.WINNERS = 0 
        self.RESULTS_STACK = []
        self.ELIMINATED_NAMES = []
        self.WINNERS_NAMES = []
        self.TOTAL_VOTES = 0
        self.THRESHOLD = 0 
        # Column corrolated to the name of the canidate (key, value) is (column value, canidate name)
        self.COLUMN_NAMES = {}
        # canidate found name 
        self.LATEST_WINNER = ""
    #######################################
    # METHOD TO RECORD DATA 
    # data_row  representing a singular ballot 
    # text_question_row a the names of the canidate above
    ###########################################
    def record_data(self, data_row): 
        ballot = RankedBallot(number_of_seats=self.NUM_OF_SEATS_OPEN)
        for column in self.COLUMNS: 
            canidate_name = self.COLUMN_NAMES[column]
            if canidate_name not in self.CANIDATE_NAMES: 
                self.CANIDATE_NAMES.append(canidate_name)
                self.ALL_BALLOTS_FOR_CANIDATE[canidate_name] = []
                self.TOP_CANIDATES_BALLOT[canidate_name] = []
            if data_row[column] != "": 
                canidate_rank = int(data_row[column])
                
                ballot.add_vote(canidate_name, canidate_rank)
                self.ALL_BALLOTS_FOR_CANIDATE[canidate_name].append(ballot) 
        if ballot.get_top_canidate_name() != None: 
            self.TOTAL_VOTES += 1 
        
            self.TOP_CANIDATES_BALLOT[ballot.get_top_canidate_name()].append( ballot)
    # RUN THE ELECTION 
    def run_election(self):
        #CALCULATE THE THRESHOLD
        self.THRESHOLD = self.getthreshold()
        # to hold information about what round we are on 
        round_counter = 0 
        # Value to set if found winner
        found_winner = False
        i = 1
        for canidate in self.CANIDATE_NAMES: 
            num_ballots = len(self.TOP_CANIDATES_BALLOT[canidate])
            self.RESULTS[i] = (canidate, num_ballots, False, num_ballots )
            i += 1
        # s
        while True: 
            
            # IF we have found enough winners, break 
            if self.WINNERS == self.NUM_OF_SEATS_OPEN or len(self.CANIDATE_NAMES) - self.ELIMINATED == self.NUM_OF_SEATS_OPEN: 
                print(f"{DIVIDER} FINISHED-- FOUND WINNERS!!!{DIVIDER}")
                print(self.print_results())
                print(f"{DIVIDER} {DIVIDER}{DIVIDER}{DIVIDER}{DIVIDER}")
                break 
            round_counter += 1

            print(f"{DIVIDER}Round #: {round_counter}{DIVIDER}" )
            print(self.print_results())
            
            # If all seats are not filled, run the election once to see if there is a winner
            found_winner = self.run_once()
           
            # if not enough winners have been found after running once, run to see if anyone is over the threshold 
            if self.WINNERS < self.NUM_OF_SEATS_OPEN or len(self.CANIDATE_NAMES) - self.ELIMINATED != self.NUM_OF_SEATS_OPEN:
                # if all canidates with the least amount of votes have been eliminated so there are only the correct number of canidates that 
                        # either are winners or have not been eliminitated yet, break 
               
                # if no winner has been found 
                if found_winner == False: 
                    #eliminate the canidate with the lowest rankings 
                    self.eliminate_canidate()
                #if at least one winner has been found
                else: 
                    # redistribute top votes 
                    self.redistribution()
        print("knosdfn")
    # Code to run election once 
    def run_once(self):
        i = 1 
        temp_Results = {} 
        winner_found = False
        
        # for each canidates ballots ranked #1 
        for  canidate in self.CANIDATE_NAMES: 
            num_ballots = 0 
            eliminated = True
            # if the canidate has not been eliminated yet
            if canidate not in self.ELIMINATED_NAMES: 
                num_ballots, weight = self.calc_weight(canidate)
                eliminated = False
                #if the weight is over or equal to the threshold
                if (weight >= self.THRESHOLD)and canidate not in self.WINNERS_NAMES: 
                    # add to winners
                    self.WINNERS += 1 
                    # add name to list of winners names 
                    self.WINNERS_NAMES.append(canidate)
                    # mark that  winner has been found 
                    self.LATEST_WINNER = canidate
                    winner_found = True
                    break
                # store in temp results after round 
            temp_Results[canidate]  = ( num_ballots, eliminated )
        # input temporary results sorted into RESULTS
        for canidate, results in sorted(temp_Results.items(), key = lambda k: k[1], reverse=True): 
            self.RESULTS[i] = [canidate, results[0], results[1], self.RESULTS[i][3]]
            i += 1 
        # Return true or false if a winner has been found 
        return winner_found
        
   
# Helper method to obtain a threshold
    def getthreshold(self):
        return ((self.TOTAL_VOTES/(self.NUM_OF_SEATS_OPEN + 1)) )+ 1

    # code to eliminate a canidate 
    def eliminate_canidate(self):
        i = len(self.CANIDATE_NAMES)
        while i != 0: 
            canidate_name = self.RESULTS[i][0]
            eliminated = self.RESULTS[i][2]
            if eliminated == False: 
                break
            i -= 1
        print(f" ELIMINATION FOR {canidate_name}")
        # for each ballot that has the canidates name ranked at somepoint 
        for ballot in self.ALL_BALLOTS_FOR_CANIDATE[canidate_name]: 
            # if it is there top choice for canidate
            if ballot.get_top_canidate_name() == canidate_name: 
                # go through the process to remove the canidate as the top choice 
                ballot.remove_top_canidate()
                
                #once that is done, give the new top canidate that ballot 
                if ballot.get_top_canidate_name() != None: 
                    self.TOP_CANIDATES_BALLOT[ballot.get_top_canidate_name()].append(ballot)
                else: 
                    del ballot
            # if it is not a canidate
            
            else: 
                # remove the canidate from the ballot
                ballot.remove_canidate_by_name(canidate_name)
        # remove the canidate from all lists of the canidate
        self.RESULTS[len(self.CANIDATE_NAMES)-self.ELIMINATED][2] = True
        self.ALL_BALLOTS_FOR_CANIDATE.pop(canidate_name)
        self.TOP_CANIDATES_BALLOT.pop(canidate_name)
        self.ELIMINATED += 1 
        self.ELIMINATED_NAMES.append(canidate_name)
    # method for redistrinbution 
    def redistribution(self): 
        # for every canidate listed as a winner 
        for canidate in self.WINNERS_NAMES:
            # calculate the weight of each ballot for that canidate
            num_ballots, total_weight = self.calc_weight(canidate)
            # if the total weight is greater than the threshold
            if total_weight > self.THRESHOLD: 
                print(f"REDISTRIBUTION FOR {canidate}")
                # aware that canidate the percent back that it is over
                percent_back = (total_weight - self.THRESHOLD)/num_ballots
                self.redistribute_votes_canidate(canidate, percent_back)
                break
    # Helper method to calculate weight
    def calc_weight(self, canidate): 
        num_ballots = 0
        total_weight = 0

        for ballot in self.TOP_CANIDATES_BALLOT[canidate]:
            if ballot.get_vote_by_name(canidate) != None:
                total_weight += ballot.get_vote_by_name(canidate).weight
                num_ballots += 1
        return num_ballots, total_weight


    # Redistribute votes for one canidate 
    def redistribute_votes_canidate(self, canidate_name, weight):
        for ballot in self.TOP_CANIDATES_BALLOT[canidate_name]: 
            #adds half a vote 
            ballot.add_halfVote(weight)
    def set_canidate_names_list(self, canidate_names=[]):
        self.CANIDATE_NAMES = canidate_names
    def get_results(self):
        return super().get_results()
    def get_name_of_election(self):
        return super().get_name_of_election()
    def get_number_of_votes(self):
        return super().get_number_of_votes()
    def get_canidate_names(self):
        return super().get_canidate_names()
    def print_results(self):
        table_top = "place -- canidate name -- Eliminated? -- Initial(%)   ----- final(%)"
        print(f"THRESHOLD: {self.THRESHOLD}")
        print(f"NUMBER OF VOTES CAST: {self.TOTAL_VOTES}")
        print(f"NUMBER OF SEATS BEING ELECTED: {self.NUM_OF_SEATS_OPEN}")

        print( table_top)

        for place, canidate_results in self.RESULTS.items(): 
            canidate_name = canidate_results[0]
            winner = 'NOT ELIMINATED'
            if canidate_results[2] == True: 
                winner = "ELIMINATED"
            results = canidate_results[1]
            inital = canidate_results[3]

            print( f"({place} -- {canidate_name}------ {winner}---- {inital}({round((inital/self.TOTAL_VOTES) *100)  }%)----- {results}({round((results/self.TOTAL_VOTES) *100)  }%)\n")

# Helper method to associate canidate name with correct column 
    def make_canidate_names_to_columns(self, text_question_row): 
        # for each column 
        for col in self.COLUMNS: 
            # for each value for the cell in the text_question row 
            question_row = text_question_row[col]
            # for each character in that celll
            for j in range(len(question_row) - 1, 0, -1):
                            # parse to canidate name 
                            if question_row[j-2:j+1] == ' - ':
                                # add to columns names 
                                self.COLUMN_NAMES[col] = question_row[j+1:]


