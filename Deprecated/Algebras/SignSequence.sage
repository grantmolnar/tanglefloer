class SignSequence:
    def __init__(self, sequence):
        for i in sequence:
            assert (i == 1) or (i == -1)
        self.sequence = list(sequence)
        self.degree = len(sequence)

        # later we need to know, given a positively oriented strand, what count positive strand this is
        npos = 0
        poscount = [-1]*len(sequence)
        for i in range(0,len(sequence)):
            if sequence[i] == 1:
                npos = npos + 1
                poscount[i] = npos
        self.poscount = poscount
        self.npos = npos

    #The length of the underlying list of +1's and -1's
    def degree(self):
        return self.degree

    #The underlying list of +1's and -1's of the sign sequence
    def sequence(self):
        return self.sequence

    #Returns the sequence which counts how many positive terms there are up to each index.
    #For instance, [-1,1,-1,1,1] -> [-1,1,-1,2,3]
    def poscount(self):
        return self.poscount

    #The number of positive terms in the sign sequence
    #For instance, [-1,1,-1,1,1] -> 3
    def npos(self):
        return self.npos

    def __getitem__(self,key):
        return self.sequence[key]

    def __len__(self):
        return self.degree

    def __str__(self):
        return str(self.sequence)

    def __repr__(self):
        return str(self.sequence)

    def __eq__(self,other):
        if (self.sequence == other.sequence): return True
        else: return False
