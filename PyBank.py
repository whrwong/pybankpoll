import pandas as pd

# get the data
bank_data = pd.read_csv("Resources/budget_data.csv")
# view, understand data 
# print(bank_data.head())


# tasks:
# calculate total # of months in ds: count rows
month_count = bank_data.count()[0]
# calculate grand total of profit/losses over the entire period: run sum function
net_total = bank_data.sum()["Profit/Losses"]

# calculate the monthly changes in profit/losses: create a for loop to loops thru all months/rows and calculate change month to month

change = 0
greatest_increase = 0
greatest_decrease = 0
date_greatest_increase = ""
date_greatest_decrease = ""

# x is month/row
for x in range(1, month_count): 
	monthly_change = bank_data["Profit/Losses"][x] - bank_data["Profit/Losses"][x-1]
	change = change + monthly_change

# calculate the greatest increase (biggest positive change) in profits: 
	if monthly_change > greatest_increase:
		greatest_increase = monthly_change
		date_greatest_increase = bank_data["Date"][x]

# calculate the greatest decrease (biggest negative change) in profits
	if monthly_change < greatest_decrease:
		greatest_decrease = monthly_change
		date_greatest_decrease = bank_data["Date"][x]

# calculate the average of the monthly changes above ^ : sum n-1 # of changes and divide by n-1
average = round(change/(month_count-1),2)


# print the results on the screen 
print("Financial Analysis")
print("---------------------------------")
print("Total Months: {} ".format(month_count))
print("Total: ${} ".format(net_total))
print("Average Change: ${} ".format(average))
print("Greatest Increase in Profits: {} (${}) ".format(date_greatest_increase, greatest_increase))
print("Great Decrease in Profits: {} (${}) ".format(date_greatest_decrease, greatest_decrease))
# export results to a text file

out_file = open("analysis_result.txt", "w") # 'w' allows us to write in the .txt
out_file.close() # without .close, the file is corrupt
out_file = open('analysis_result.txt', "at") # 'at' allows us to add new lines to existing file (append text)
out_file.write('\nFinancial Analysis') # \n includes what we want to write
out_file.write('\n-----------------------------')
out_file.write('\nTotal Months: {} '.format(month_count))
out_file.write('\nTotal: $ {} '.format(net_total))
out_file.write('\nAverage Change: {}'.format(average))
out_file.write('\nGreatest Increase in Profits: {} (${})'.format(date_greatest_increase, greatest_increase))
out_file.write('\nGreatest Decrease in Profits: {} (${})'.format(date_greatest_decrease, greatest_decrease))
out_file.write('\n-----------------------------')
out_file.close()