
#import dependencies 
import os
import csv 

#create file path
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")
revenue_change =[]
last_loss = 0

#read csv

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    

    P = []
    months = []

    #read through each row
    for row in csvreader:
        P.append(int(row[1]))
        months.append(row[0])

    

    for x in range(1, len(P)):
        revenue_change.append((int(P[x])- int(P[x-1])))

    rev_average = sum(revenue_change) / len(revenue_change)
    total_months = len(months)

    max_increase = max(revenue_change)
    min_decrease = min(revenue_change)


#print results 
print("Financial Analysis")

print("-------------------------------------")

print("total months:" + str(total_months))

print("total: " + "$" + str(sum(P)))

print("average change: " + "$" + str(rev_average))

print("greatest increase in profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(max_increase))

print("greatest decrease in profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(min_decrease))

#create output file

file = open("output.txt","w")

file.write("Financial Analysis" + "\n")

file.write("........................................................." + "\n")

file.write("total months: " + str(total_months) + "\n")

file.write("Total: " + "$" + str(sum(P)) + "\n")

file.write("Average change: " + "$" + str(rev_average) + "\n")

file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(max_increase) + "\n")

file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(min_decrease) + "\n")

