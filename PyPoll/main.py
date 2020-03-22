import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

candidates = []

with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    csv_no_header = next(csvreader, None)

    for row in csvreader:
        candidates.append(str(row[2]))

    #total_voters = (len(list(csvreader)) + 1)

candDic = {}
names = []
vote_str = []
vote = []
vote_perc = []

for i in candidates:
    if i in candDic:
        candDic[i]+=1
        #candDic[i] = candDic[i] + 1
    else:
        candDic[i] = 1

for i in candDic.keys():
    vote_str.append(candDic[i])
    names.append(str(i))

for i in vote_str:
    vote.append(int(i))

total_voters = sum(vote)

for i in vote_str:
    vote.append(int(i))

for i in vote:
    vote_perc.append(round((i / total_voters) * 100, 3))
    
#vote_max = 0
vote_max = max(vote_perc)

for i in range(len(vote_perc)):
    if vote_perc[i] == vote_max:
        winner = names[i]

print("Election Results")
print("-" * 25)
print(f'Total Votes: {total_voters}')
print("-" * 25)
for i in range(len(names)):
    print(f'{names[i]}: {vote_perc[i]}% ({vote[i]})')
print("-" * 25)
print(f'Winner: {winner}')
print("-" * 25)


output_path = os.path.join('Resources', 'output_election_data.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =",")
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes:', total_votes])
    csvwriter.writerow([])
    for i in range(len(names)):
        csvwriter.writerow([names[i], str(votes_perc[i])+'%', vote[i]])
    csvwriter.writerow(["Winner: ", winner])