


import os
import csv

# join path 

election_data = os.path.join('PyPoll', 'resources', 'election_data.csv')


cand_votes = {}
cand_list = []
total_votes = 0
winner = ""
win_perc = 0 
win_count = 0


#read csv

with open(election_data, 'r') as csvfile:
    elec_data = csv.reader(csvfile, delimiter =',')
    header = next(elec_data)

    stockham_count= 0
    degette_count = 0
    doane_count = 0
    stockham_perc = 0
    degette_perc = 0 
    doane_perc = 0
 

    for row in elec_data:
       total_votes += 1
       candidate_name =row[2]

       if row [2] == "stockham":
            stockham_count += 1
       elif row[2] == "degette":
            degette_count += 1
       elif row[2] == "doane":
            doane_count += 1


       #if candidate_name not in cand_list:
           ##cand_votes[candidate_name] = 0
           #cand_votes[candidate_name] += 1

results = {"stockham":stockham_count, "degette":degette_count, "doane":doane_count}

print(results)

for candidate_name in cand_votes:
    vote_count = cand_votes[candidate_name]

    vote_per = (vote_count) / (total_votes) * 100
    cand_results = f"{candidate_name}: {vote_per:.1f}% ({vote_count:,})\n"
    #print(f"{candidate_name}: {vote_per}")
       

stockham_perc = round((stockham_count / total_votes) * 100, 3)

