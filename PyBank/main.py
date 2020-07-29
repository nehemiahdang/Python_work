# Import dependencies
import os
import csv

# Save the csv path into a variable
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Create variables for potential usage
total_months = 0
total_amount = 0
greatInc = 0
greatInc_month = 0
greatDec = 0
greatDec_month = 0
total_change = 0
average_change = 0
daily_change = 0
changes = []
dates = []

# Read the csv path
with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    # Loop through the csvreader; appends the data into the array for the 2 columns
    for row in csvreader:
        # Counts the months to get the total as it loops to each row
        total_months += 1
        
        # Adds the profit/losses row to the variable to get the total as it loops to each row
        total_amount = total_amount + int(row[1])

        # Append profit/losses column and convert to float value; subtract the row with the daily change to get the difference
        changes.append(float(row[1]) - daily_change)
        daily_change = float(row[1])

        # Append the dates column
        dates.append(row[0])

# Loop through the changes list, but exclude the first on the list because it isn't affected the daily_change
for i in range(1, len(changes)):
    total_change += changes[i]

    # Changes the greatest increase, if the change is higher than the previous; changes the date if true
    if greatInc < changes[i]:
        greatInc = int(changes[i])
        greatInc_month = dates[i]

    # Changes the greatest decrease, if the change is lower than the previous; changes the date if true
    elif greatDec > changes[i]:
        greatDec = int(changes[i])
        greatDec_month = dates[i]

# Get the average change from the total change and total months minus 1, because the first month doesn't have a previous month to compare to
average_change = round(total_change / (total_months-1), 2)

# Print the final analysis
print("Financial Analysis")
print("-" * 25)
print(f'Total Months: {total_months}')
print(f'Total: $ {total_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatInc_month} (${greatInc})')
print(f'Greatest Decrease in Profits: {greatDec_month} (${greatDec})')

# Load the output csv; write the final analysis into the csv
output_path = os.path.join('Resources', 'output_budget_data.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =",")
    csvwriter.writerow(['Total Months', total_months])
    csvwriter.writerow(['Total', total_amount])
    csvwriter.writerow(['Average Change', average_change])
    csvwriter.writerow(['Greatest Increase in Profits', greatInc_month, greatInc])
    csvwriter.writerow(['Greatest Decrease in Profits', greatInc_month, greatInc])