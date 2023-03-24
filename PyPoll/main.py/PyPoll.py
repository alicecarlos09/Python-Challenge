


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

   
 

    for row in elec_data:
       total_votes += 1
       candidate_name =row[2]

       


       if candidate_name not in cand_list:
               cand_list.append(candidate_name)

               cand_votes[candidate_name] = 0
       cand_votes[candidate_name] += 1





for candidate_name in cand_votes:
    vote_count = cand_votes[candidate_name]

    vote_per = float(vote_count) / float(total_votes) * 100
    cand_results = f"{candidate_name}: {vote_per:.1f}% ({vote_count:,})\n"
    print(cand_results)

    if (vote_count > win_count) and (vote_per > win_perc):
         win_count = vote_count
         winner = candidate_name
         win_perc = vote_per

    


    print("Election Results")
    print("--------------------------")
    print(cand_results)
    print("Winner:" + (winner))
    print(total_votes)


file = open("output_pypoll.txt", "w")
file.write("Election Results" + "\n")
file.write("........................................................." + "\n")
file.write(cand_results + "\n")
file.write(winner)
file.write(str(total_votes))




     




