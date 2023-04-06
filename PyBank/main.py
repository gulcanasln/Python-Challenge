import os 
import csv 

#path to collect data from resources folder

csvpath= os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csvheader=next(csvreader)

    revenue=[]
    date=[]
    rev_change=[]

    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])

    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change= round(sum(rev_change)/len(rev_change),2)
        max_rev_change=round(max(rev_change))
        min_rev_change=round(min(rev_change))
        max_rev_change_date= str(date[rev_change.index(max(rev_change))])
        min_rev_change_date=str(date[rev_change.index(min(rev_change))])

multiline_str= (
"Financial Analysis\n"
'...................\n'
f'Total Months: {len(date)}\n'
f"Total: ${round(sum(revenue))}\n"
f'Average Change: ${avg_rev_change}\n'
f'Greatest Increase in Profits: {max_rev_change_date} (${max_rev_change})\n'
f'Greatest Decrease in Profits: {min_rev_change_date} (${min_rev_change})\n'
)

print(multiline_str, end="")

output_text = os.path.join("analysis", "financial_analysis.txt")
file1 = open(output_text, "w")
file1.write(multiline_str)
file1.close()
