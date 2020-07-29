# Import dependencies
import os
import csv

# Save the csv path into a variable
election_csv = os.path.join('Resources', 'election_data.csv')

# Create variables for potential usage
candidates = []
cand_dict = {}
names = []
vote_totals = []
votes_perc = []
total_voters = 0

# Read the csv path
with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    # Loop through the csvreader; appends the data into the array for the column we're going to use
    for row in csvreader:
        candidates.append(str(row[2]))

# Loop through the collected data
for candidate in candidates:
    if candidate not in cand_dict:
        # Adds the candidate name if it's not in the dictionary
        cand_dict[candidate] = 1
    else:
        # Adds to the counter if the candidate's name appears per loop
        cand_dict[candidate] += 1

# Loop through the keys for the cand_dict dictionary
for candidate in cand_dict.keys():
    # Append the names of the candidates and convert it to string
    names.append(str(candidate))
    # Use the name of the candidate to parse through the dictionary to get the number of votes and append
    vote_totals.append(cand_dict[candidate])

# Get the total number of voters
total_voters = sum(vote_totals)

# Loop through the vote totals to get the percentage for each candidate
for votes in vote_totals:
    votes_perc.append(round((votes / total_voters) * 100, 3))

# Get the length of the votes percent array and use it for the loop
for i in range(len(votes_perc)):
    # If the index of the votes_perc is the highest, then we have our winner!
    if votes_perc[i] == max(votes_perc):
        winner = names[i]

# Print the final analysis
print("Election Results")
print("-" * 25)
print(f'Total Votes: {total_voters}')
print("-" * 25)
for i in range(len(names)):
    print(f'{names[i]}: {votes_perc[i]}% ({vote_totals[i]})')
print("-" * 25)
print(f'Winner: {winner}')
print("-" * 25)

# Load the output csv; write the final analysis into the csv
output_path = os.path.join('Resources', 'output_election_data.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =",")
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes:', total_voters])
    for i in range(len(names)):
        csvwriter.writerow([names[i], str(votes_perc[i])+'%', vote_totals[i]])
    csvwriter.writerow(["Winner: ", winner])