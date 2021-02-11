import csv
import os

poll_file = os.path.join("Resources", "election_data.csv")

tot_votes = 0
cand_list = []
cand_votes = {}
cand_per = {}
winner = " "
win_vote = 0

with open(poll_file) as data:
    csvreader = csv.reader(data)

    header = next(csvreader)

    for row in csvreader:

        tot_votes = tot_votes + 1

        cand_name = row[2]

        if cand_name not in cand_list:

            cand_list.append(cand_name)

            cand_votes[cand_name] = 0
        cand_votes[cand_name] = cand_votes[cand_name] + 1
        cand_per[cand_name]=round(cand_votes[cand_name] * 100/tot_votes,2)
print(cand_list)
print(cand_votes)
print(tot_votes)
print(cand_per)

for candidate in cand_votes:
    votes = cand_votes.get(candidate)

    if(votes > win_vote):
        win_vote = votes
        winner = candidate

    for candidate in cand_per:
        percentage = cand_per.get(candidate)


    vote_recd = f"{candidate}:{percentage}%({votes})"
    print(vote_recd)

    



