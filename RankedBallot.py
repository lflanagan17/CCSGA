# Object to hold data about a vote 

class Vote:
    def __init__(self, canidate, rank, weight=1): 
        # holds the canidate name for the vote
        self.canidate =canidate
        # the number for their ranking on the ballot (if someone ranked them 1st, 2nd, etc)
        self.rank = rank
        # the weight of that vote (i.e. if a canidate redistributes a partial vote to another canidate )
        self.weight = weight
    # adds or subtracts from the weight value
    def add_weight(self, weight): 
        self.weight += weight 
    # updates the canidate rank
    def change_rank(self, rank): 
        self.rank = rank




# object for a singular ranked ballot 

class RankedBallot:
    def __init__(self, number_of_seats=1):
        # for a certain election, a ballot will know how many seats are open 
        self.number_of_seats = number_of_seats
        self.votes = [] # contains a list of vote objects
    # adding a vote to a ballot
    def add_vote(self, candidate_name, rank):
        i = 0
        #for multi seat ranked seats, if the rank is greater than the number of seats, disregard 
        if rank > self.number_of_seats or self.number_of_seats != 1:
            return
        # add the vote into the list in order
        while i < len(self.votes) and rank > self.votes[i].rank:
            i += 1
        # add a new vote tothe list. A weight will be initlized to 1 always
        self.votes.insert(i, Vote(candidate_name, 1, rank))
    # adds a partion of a vote to the weight for a ballot
    def add_halfVote(self, i):
        # As long as there is more than one vote remaining in ballot
        if len(self.votes) > 1: 
            # add the weight to the second choice canidate 
            self.votes[1].add_weight(i )
            # remove it from the top canidate 
            self.votes[0].add_weight( -i)
       
    def is_empty(self):
        return len(self.votes) == 0
    # gets their first choice canidate
    def get_top_canidate_name(self):
        if self.is_empty(): 
            return None 
        return self.votes[0].canidate
    def get_vote_by_name(self, canidate_name): 
        vote_selected = None
        for vote in self.votes: 
            if vote.canidate == canidate_name:
                vote_selected = vote
        return vote_selected
    # returns the vote
    def get_vote(self, rank:int):
        return self.votes[rank-1]
    def remove_top_canidate(self):
        if len(self.votes) == 0: 
            return False
        else:  
            return self.remove_canidate(0)
  

    def remove_canidate_by_rank(self, rank):
        if len(self.votes) == 0: 
            return False
        else:  
            i =0
            for vote in self.votes: 
                if vote.rank == rank: 
                    return self.remove_canidate(i)
                i += 1
            return False
    def remove_canidate_by_name(self, canidate_name): 
        i = 0 
        
        for vote in self.votes: 
            if vote.canidate == canidate_name: 
                return self.remove_canidate(i)
            i += 1
         
        return False
    # method to remove a canidate and update their rank 
    def remove_canidate(self, vote_position): 
        del self.votes[vote_position]
        while vote_position < len(self.votes): 
                self.votes[vote_position].change_rank(- 1) 
                vote_position+= 1
        return True