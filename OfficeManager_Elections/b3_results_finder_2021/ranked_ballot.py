class RankedBallot:

    def __init__(self):
        self.votes = [] # to contain (candidate_name, rank) tuples

    def add_vote(self, candidate_name, rank=int):
        i = 0
        while i < len(self.votes) and rank > self.votes[i][1]:
            i += 1
        self.votes.insert(i, (candidate_name, rank))
    
    def is_empty(self):
        return len(self.votes) == 0
    
    def get_top_candidate_name(self):
        return self.votes[0][0]

    def remove_top_candidate(self):
        del self.votes[0]
        return self.is_empty()
