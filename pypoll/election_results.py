import os
import csv

dirname = os.path.dirname(__file__)
elecdata_csv = os.path.join(dirname, 'Resources', 'election_data.csv')

with open(elecdata_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')  # Split the data on commas
    total_votes = 0
    candidates = []
    votes=[]                                        #initialise all value on variables
    candidate_votes = []                            #used list for most of the variables as there are multiple data
    candidate_vote_perc = []
    winner = ""
    next(csvfile)

    for row in csvreader:                           #first loop to get total votes
        total_votes += 1

        if row[2] not in candidates:                #and get unique individual candidates in the csv 
            candidates.append(row[2])

        votes.append(row[2])                        #adds number of votes accodingly, without this the next loop won't work

    for individual in candidates:                   #second loop to count all votes for each individual
        candidate_votes.append(votes.count(individual))
        candidate_vote_perc.append(round(votes.count(individual)/total_votes*100, 2))   #as well as the percentage
        
            
winner = candidates[candidate_votes.index(max(candidate_votes))]    #get the winner using MAX within the index
    
#time to print out the result on the terminal    
print(f'Election Results')
print(f'---------------------')
print(f'Total Votes: {total_votes}')
for i in range (len(candidates)):
    print(f'{candidates[i]}: {candidate_vote_perc[i]}% ({candidate_votes[i]})')
print(f'---------------------')
print(f'Winner: {winner} ')

#the following is to output the result to a text file - output.txt
out = open("C:/Users/bluec/python-challenge/PyPoll/analysis/output.txt", "w")
out.write(f'Election Results\n')
out.write(f'---------------------\n')
out.write(f'Total Votes: {total_votes}\n')
for i in range (len(candidates)):
    out.write(f'{candidates[i]}: {candidate_vote_perc[i]}% ({candidate_votes[i]})\n')
out.write(f'---------------------\n')
out.write(f'Winner: {winner} \n')
out.close()