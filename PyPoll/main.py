# Import the os Module
import os

# Import Module for reading CSV files
import csv
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Improved CSV file
with open (csvpath, newline='') as csvfile:

#CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')

# Add new variables
    Votes_count = 0
    votes = []
    Voted_candidates = []
    Votes_share = []
    Winner = " "

# Compute the total number of votes cast
    next(csvreader,None)
    for x in csvreader:
        if x[-1] not in Voted_candidates:
            Voted_candidates.append (x[-1])
            votes.append(1)
        else:
            index = Voted_candidates.index(x[-1])
            votes[index] += 1
        Votes_count += 1
    print('TOTAL VOTES')
    print(Votes_count)

#List voted candidates
    print('VOTED CANDIDATES')
    print(Voted_candidates)

# Compute the percentage of votes each candidate got
    for y in votes:
        shares = '{0:.3f}'.format(round((y/Votes_count)*100,2))
        Votes_share.append(shares)
    print('SHARE OF VOTES')
    print(Votes_share)
    print("TOTAL VOTES")
    print(votes)
