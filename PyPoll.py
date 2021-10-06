import pandas as pd

poll_data = pd.read_csv('PyPoll_Resources_election_data.csv')
# print(poll_data.head())

total_votes = poll_data.count()['Voter ID']
# print(poll_data.groupby('Candidate').count())

# the groupby and count functions create a pivot table with the count of votes for each candidate
votes_by_candidate = poll_data.groupby('Candidate').count()

# change the column names to prepare it for the final output
votes_by_candidate = votes_by_candidate.rename(columns = {"Voter ID": "Voter Count", "County": "Percent"})
# print(votes_by_candidate)

# sort rows by Percent from highest to lowest (descending) - sort candidates by vote count
votes_by_candidate = votes_by_candidate.sort_values(by=['Percent'],ascending=False)

# calculate the Percent of votes each candidate received
votes_by_candidate.loc[:,'Percent'] = round((votes_by_candidate.loc[:,'Voter Count']/total_votes)*100,0)
# print(votes_by_candidate)
# print("\n")


print('Election Results')
print('------------------------')
print('Total Votes: {}'.format(total_votes))
print('------------------------')
for j in range(0, len(votes_by_candidate)):
	print('{}: {}00% ({})'.format(votes_by_candidate.index[j], votes_by_candidate['Percent'][j], votes_by_candidate['Voter Count'][j]))
print('------------------------')
print('Winner: {}'.format(votes_by_candidate.index[0]))
print('------------------------')


out_file = open("election_result.txt", "w")
out_file.close()
out_file = open('election_result.txt', "at")
out_file.write('\nElection Results')
out_file.write('\n-----------------------------')
for j in range(0, len(votes_by_candidate)):
	out_file.write('\n{}: {}00% ({})'.format(votes_by_candidate.index[j], votes_by_candidate['Percent'][j], votes_by_candidate['Voter Count'][j]))
out_file.write('\n-----------------------------')
out_file.write('\nWinner: {}'.format(votes_by_candidate.index[0]))
out_file.write('\n-----------------------------')
out_file.close()