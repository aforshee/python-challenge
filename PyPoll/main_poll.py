
#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, 
# his concentration isn't what it used to be.)

#You will be give a set of poll data called election_data.csv. 
#The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

#In addition, your final script should both print the analysis to the terminal
#and export a text file with the results.

#import modules
import os
import csv

#create environmnet to get data
dirpath = os.path.dirname(os.path.realpath(__file__))
#input file
input_file = os.path.join(dirpath, '03-Python_homework_assignment_PyPoll_Resources_election_data (1).csv')

#output file
output_file = os.path.join(dirpath,"A.Forshee.PollResults.txt")

#create lists
#The total number of votes cast
Votes = []
#The total number of votes each candidate won
Khan_votes = []
Corey_votes = []
Li_votes = []
OTooley_votes = []
disinct_candidates = []

#read csv file, use encoding = 'utf-8'
with open(input_file, encoding ='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header
    csv_header = next(csvfile)
    #total number of votes cast
    for row in csvreader:
        Votes.append(row[0])
        if row[2] == 'Khan':
            Khan_votes.append(row[2])
        if row[2] == 'Correy':
            Corey_votes.append(row[2])
        if row[2] == 'Li':
            Li_votes.append(row[2])
        if row[2] == "O'Tooley":
            OTooley_votes.append(row[2])
    


Total_Votes = (len(Votes))
Total_Khan = (len(Khan_votes))
Total_Corey = (len(Corey_votes))
Total_Li = (len(Li_votes))
Total_OTooley = (len(OTooley_votes))

#Percentages for each candidate
Percentage_Khan = str(len(Khan_votes)/len(Votes))
Percentage_Correy = str(len(Corey_votes)/len(Votes))
Percentage_Li = str(len(Li_votes)/len(Votes))
Percentage_OTooley = str(len(OTooley_votes)/len(Votes))

#List of Candidates
cand_dict = {'Khan': Total_Khan, 
                'Correy': Total_Corey, 
                'Li': Total_Li, 
                'OTooley': Total_OTooley}
win_percent = 0
winner = 'unknown'
for key, value in cand_dict.items():
    if value > win_percent:
        win_percent = value
        winner = key

print("Total Votes: " + str(Total_Votes))
print("Khan Votes: " + str(Total_Khan))
print("Correy Votes: " + str(Total_Corey))
print("Li Votes: " + str(Total_Li))
print("O'Tooley Votes: " + str(Total_OTooley))
print("Khan Percentage: " + Percentage_Khan)
print("Correy Percentage: " + Percentage_Correy)
print("Li Percentage: " + Percentage_Li)
print("O'Tooley: " + Percentage_OTooley)
print("And the winner is: " + winner)

# Printing to text file
with open(output_file,'w') as textfile:
    print("Total Votes: " + str(Total_Votes), file=textfile)
    print("Khan Votes: " + str(Total_Khan), file=textfile)
    print("Correy Votes: " + str(Total_Corey), file=textfile)
    print("Li Votes: " + str(Total_Li), file=textfile)
    print("O'Tooley Votes: " + str(Total_OTooley), file=textfile)
    print("Khan Percentage: " + Percentage_Khan, file=textfile)
    print("Correy Percentage: " + Percentage_Correy, file=textfile)
    print("Li Percentage: " + Percentage_Li, file=textfile)
    print("O'Tooley: " + Percentage_OTooley, file=textfile)
    print("And the winner is: " + winner, file=textfile)
