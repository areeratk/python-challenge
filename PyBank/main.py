import os
import csv
import statistics

# Path to collect data from the Resources folder
profits_losses_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(profits_losses_csv, newline="") as csvfile:
    #Split the data on comma
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    csv_header = next(csvfile)
    
    #Initialize variable to hold Date and Profits/Losses values
    total_months = 0
    total_profits = 0
    lastmonth_profits = 0
    lastmonth = 0
    change_profits = []
    change_month = []
               
    # Read through each row of data after the header and loop through the data
    for row in csvreader:
        #Find the total number of months
        total_months += 1
        #Find the net total amount of profits and losses
        total_profits += int(row[1])
        #Find the changes of profits and losses
        currentmonth_profits = int(row[1])
        current_month = (str(row[0]))
        if lastmonth_profits != 0:
            change_profits.append(currentmonth_profits - lastmonth_profits)         
            change_month.append(current_month)
        lastmonth_profits = currentmonth_profits
        lastmonth = current_month
    
    #Find the average changes of profits and losses over the entire period
    average_change_profits = round(statistics.mean(change_profits),2)
 
    #Find the greatest increase in profits (date and amount) over the entire period
    greatest_increase_profits = max(change_profits)
    greatest_increase_profits_month = change_month[change_profits.index(greatest_increase_profits)]
    
    #Find the greatest decrease in profits (date and amount) over the entire period
    greatest_decrease_profits = min(change_profits)
    greatest_decrease_profits_month = change_month[change_profits.index(greatest_decrease_profits)]
    
    # Print the result in terminal
    print("-------------------")
    print(f"Financial Analysis")
    print("------------------------------------------------------")
    
    print(f"Total Months: {str(total_months)}")
    print(f"Total Profits: ${str(total_profits)}")   
    print(f"Average Change: ${str(average_change_profits)}")
    print(f"Greatest Increase in Profits: {greatest_increase_profits_month}  $({greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_profits_month}  $({greatest_decrease_profits})")
    print("------------------------------------------------------")

