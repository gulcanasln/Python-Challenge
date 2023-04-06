import os
import csv

#path to collect data from resources folder

csvpath=os.path.join('Resources','election_data.csv')

#list to store data

total_votes=0
candidates_unique=[]
candidate_votes=[]


#read in the CSV file

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    #loop through the data
    for row in csvreader:
        #define function to calculate total votes 
        total_votes += 1
        candidate_in=(row[2])
        if candidate_in in candidates_unique:
            candidate_index=candidates_unique.index(candidate_in)
            candidate_votes[candidate_index]=candidate_votes[candidate_index]+1
        else:
            candidates_unique.append(candidate_in)
            candidate_votes.append(1)

#define function to create a list

percentage=[]
max_votes=candidate_votes[0]
max_index=0

#loop through the data

for x in range(len(candidates_unique)):
    vote_percantage=round(candidate_votes[x]/total_votes*100,2)
    percentage.append(vote_percantage)
    if candidate_votes[x]>max_votes:
        max_votes=candidate_votes[x]
        max_index=x

election_winner = candidates_unique[max_index] 

# Final script should both print the analysis to the terminal and export a text file with the results

print('Election Results')
print('-------------------------')
print(f'Total Votes:{total_votes}')
print('-------------------------')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]}:{percentage[x]:.3f}%({candidate_votes[x]})')
print('-------------------------')
print(f'Winner:{election_winner}')
print('-------------------------')

output_file = os.path.join("analysis", "election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('-------------------------\n')
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Winner: {election_winner}\n')
    datafile.write('-------------------------\n')


