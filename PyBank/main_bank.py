
#In this challenge, you are tasked with creating a Python script for analyzing the financial records of 
# your company. You will give a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#In addition, your final script should both print the analysis to the terminal
#and export a text file with the results.

#import  modules
import os
import csv

#create the environment to get the data (filepath, csv, etc)
dirpath = os.path.dirname(os.path.realpath(__file__))
# Input file
input_file = os.path.join(dirpath,'03-Python_homework_assignment_PyBank_Resources_budget_data.csv')
# Output file
output_file = os.path.join(dirpath,"A.Forshee.BankResults.txt")

# Create lists to store the number of months, net total, averages
Months = []
Profit_Loss = []
PL_Changes = []

# Reading the csv file, use encoding = 'utf-8'
with open(input_file, encoding ='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header
    csv_header = next(csvfile)

    # number of months and profit loss
    for row in csvreader:
        Months.append(row[0])
        Profit_Loss.append(float(row[1]))

# Calculating the changes in P&L
PL_Changes = [Profit_Loss[x+1]-Profit_Loss[x] for x in range(len(Profit_Loss)-1)]
New_list = zip(Months[1:],PL_Changes)
Increase = max(PL_Changes)
Decrease = min(PL_Changes)
# Finding the month
for row in New_list:
    if row[1]==Increase:
        Increase_Month = row[0]
    elif row[1] == Decrease:
        Decrease_Month = row[0]
# Summarizing all the values
total_month = str(len(Months))
total_prof_loss = sum(Profit_Loss)
average_changes = sum(PL_Changes) / len(PL_Changes)
Increase = max(PL_Changes)
Decrease = min(PL_Changes)
# Printing to the terminal 
print("Total Months: " + total_month)
print("Net Profit/Losses: " + "$" + str(total_prof_loss))
print("Average  Change: " + str(average_changes))
print("Greatest Increase in Profits: " + str(Increase_Month) + " $" + str(Increase))
print("Greatest Decrease in Profits: " + str(Decrease_Month) + " $" + str(Decrease))
# Printing to text file
with open(output_file,'w') as textfile:
    print("Total Months: " + total_month, file=textfile)
    print("Net Profit/Losses: " + str(total_prof_loss), file=textfile)
    print("Average  Change: " + str(average_changes), file=textfile)
    print("Greatest Increase in Profits: " + str(Increase_Month) + " (" + str(Increase) + ")",file=textfile)
    print("Greatest Decrease in Profits: " + str(Decrease_Month) + " (" + str(Decrease) + ")",file=textfile)