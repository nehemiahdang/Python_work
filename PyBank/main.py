import os
import csv

bank_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_amount = 0
greatInc = 0
greatDec = 10**9
average_change = 0
daily_change = 0
changes = []
dates = []

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    csv_no_header = next(csvreader, None)

    for row in csvreader:
        total_months += 1
        total_amount = total_amount + int(row[1])
        changes.append(float(row[1])-daily_change)
        daily_change = float(row[1])
        dates.append(row[0])

for i in range(1, len(changes)):
    average_change = average_change + changes[i]

    if greatInc < changes[i]:
        greatInc = int(changes[i])
        greatInc_month = dates[i]
    elif greatDec > changes[i]:
        greatDec = int(daily_change[i])
        greatDec_month = dates[i]
average_change = round(average_change / (total_months-1), 2)
print("Financial Analysis")
print("-" * 25)
print(f'Total Months: {total_months}')
print(f'Total: $ {total_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatInc_month} (${greatInc})')
print(f'Greatest Decrease in Profits: {greatDec_month} (${greatDec})')


output_path = os.path.join('Resources', 'budget_data.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =",")
    csvwriter.writerow(['Total Months', total_months])
    csvwriter.writerow(['Total', total_amount])
    csvwriter.writerow(['Average Change', average_change])
    csvwriter.writerow(['Greatest Increase in Profits', greatInc_month, greatInc])
    csvwriter.writerow(['Greatest Decrease in Profits', greatInc_month, greatInc])