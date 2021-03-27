import os
import csv

dirname = os.path.dirname(__file__)
elecdata_csv = os.path.join(dirname, 'Resources', 'election_data.csv')

with open(elecdata_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    total_votes = 0
    candidates = []
    votes=[]
    candidate_votes = []
    candidate_vote_perc = []
    winner = ""
    next(csvfile)

    for row in csvreader: 
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])

        votes.append(row[2])

    for individual in candidates:
        candidate_votes.append(votes.count(individual))
        candidate_vote_perc.append(round(votes.count(individual)/total_votes*100, 2))
        
            
winner = candidates[candidate_votes.index(max(candidate_votes))]
    
    
print(f'Election Results')
print(f'---------------------')
print(f'Total Votes: {total_votes}')
for i in range (len(candidates)):
    print(f'{candidates[i]}: {candidate_vote_perc[i]}% ({candidate_votes[i]})')
print(f'---------------------')
print(f'Winner: {winner} ')


out = open("C:/Users/bluec/python-challenge/PyPoll/analysis/output.txt", "w")
out.write(f'Election Results\n')
out.write(f'---------------------\n')
out.write(f'Total Votes: {total_votes}\n')
for i in range (len(candidates)):
    out.write(f'{candidates[i]}: {candidate_vote_perc[i]}% ({candidate_votes[i]})\n')
out.write(f'---------------------\n')
out.write(f'Winner: {winner} \n')
out.close()