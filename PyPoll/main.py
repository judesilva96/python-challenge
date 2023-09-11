import os
import csv


file = 1

poll = {}


initial_votes = 0


file_to_load = os.path.join("Resources", "election_data.csv")

with open(file_to_load, 'r') as csvfile:

    csvread = csv.reader(csvfile)

    
    next(csvread, None)

    
    for row in csvread:
        initial_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
    
candidates = []
vote_count = []


for key, value in poll.items():
    candidates.append(key)
    vote_count.append(value)


percent = []
for n in vote_count:
    percent.append(round(n/initial_votes*100, 1))


clean_data = list(zip(candidates, vote_count, percent))


winners = []

for name in clean_data:
    if max(vote_count) == name[1]:
        winners.append(name[0])


winner = winners[0]


if len(winners) > 1:
    for w in range(1, len(winners)):
        winner = winner + ", " + winners[w]


output_file = os.path.join('election_results_' + str(file) +'.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(initial_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')


with open(output_file, 'r') as readfile:
    print(readfile.read())
