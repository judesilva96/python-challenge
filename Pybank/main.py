import os 
import csv


#find the file
file_to_load = os.path.join("Resources", "budget_data.csv")

with open(file_to_load, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)


    #to hold the list of data
    number_months = []
    total_profit = []
    changes = []
    

    for row in csvreader:
        number_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        changes.append(total_profit[i+1]-total_profit[i])


 
    min_change = min(changes)
    max_change = max(changes)

    month_increase = changes.index(max(changes))+1
    month_decrease = changes.index(min(changes))+1


    print("Financial Analysis")
    print("------------------------")
    print(f"Months:{len(number_months)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Change: {round(sum(changes)/len(changes),2)}")
    print(f"Greatest Increase in Profits: {number_months[month_increase]} (${(str(max_change))})")
    print(f"Greatest Decrease in Profits: {number_months[month_decrease]} (${(str(min_change))})") 
 
    output = os.path.join(".", 'output.txt')
    with open(output,"w") as new:
        new.write("Financial Analysis")
        new.write("\n")
        new.write("------------------------")
        new.write("\n")
        new.write(f"Total Months:{len(number_months)}")
        new.write("\n")
        new.write(f"Total: ${sum(total_profit)}")
        new.write("\n")
        new.write(f"Average Change: {round(sum(changes)/len(changes),2)}")
        new.write("\n")
        new.write(f"Greatest Increase in Profits: {number_months[month_increase]} (${(str(max_change))})")
        new.write("\n")
        new.write(f"Greatest Decrease in Profits: {number_months[month_decrease]} (${(str(min_change))})")  



        