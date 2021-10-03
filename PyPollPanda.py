import pandas as pd

poll_data = pd.read_csv('Resources/PyPoll_Resources_election_data.csv')
print(poll_data.head())

#total_votes = poll_data.count()[0]
total_votes = len(poll_data)
print(total_votes)

poll_data_sorted = poll_data.set_index('Candidate')
poll_data_sorted = poll_data_sorted.sort_values(by=['Candidate'])
print(poll_data_sorted.head())
print(poll_data_sorted.tail())


d = {'name': [], 'votes': [], 'percent': []}
vote_result = pd.DataFrame(data=d, columns = ['name','votes','percent'])
# print(vote_result)

new_row = {'name':poll_data_sorted.index[0], 'votes': 0, 'percent':0}
# print(new_row)

vote_result = vote_result.append(new_row, ignore_index=True)
# print(vote_result)

nth_candidates = 0
votes = 1

n=1
while n < total_votes:
	if poll_data_sorted.index[n] == vote_result['name'][nth_candidates]:
		votes=votes+1
		n = n +1
	else:
		vote_result.loc[nth_candidates:nth_candidates, 'votes']=votes
		#vote_result['votes'][nth_candidates]=votes
		new_row = {'name':poll_data_sorted.index[n], 'votes':0, 'percent':0}
		vote_result = vote_result.append(new_row, ignore_index=True)
		nth_candidates = nth_candidates + 1
		votes = 1
		n = n+1

#vote_result['votes'][nth_candidates]=votes
vote_result.loc[nth_candidates:nth_candidates, 'votes']=votes

for i in range(0,len(vote_result)):
	vote_result.loc[i:i,'percent']=round((vote_result['votes'][i]/total_votes)*100,0)
	#vote_result['percent'][i]=round((vote_result['votes'][i]/total_votes)*100,0)
vote_result = vote_result.sort_values(by=['votes'], ascending=False)

vote_result = vote_result.set_index('name')

print('Election Results')
print('------------------------')
print('Total Votes: {}'.format(total_votes))
print('------------------------')
for j in range(0, len(vote_result)):
	print('{}: {}00% ({})'.format(vote_result.index[j], vote_result['percent'][j], vote_result['votes'][j]))
print('------------------------')
print('Winner: {}'.format(vote_result.index[0]))
print('------------------------')

out_file = open("PyPoll/Resources/election_result.txt", "w")
out_file.close()
out_file = open('PyPoll/Resources/election_result.txt', "at")
out_file.write('\nElection Results')
out_file.write('\n-----------------------------')
for j in range(0, len(vote_result)):
	out_file.write('\n{}: {}00% ({})'.format(vote_result.index[j], vote_result['percent'][j], vote_result['votes'][j]))
out_file.write('\n-----------------------------')
out_file.write('\nWinner: {}'.format(vote_result.index[0]))
out_file.write('\n-----------------------------')
out_file.close()