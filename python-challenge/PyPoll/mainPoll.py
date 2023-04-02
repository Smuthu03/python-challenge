## PyPoll
import os
import csv
import math
import string
import pathlib
from pathlib import Path

pollpath = pathlib.Path('C:/users/shara/PythonStuff/python-challenge/PyPoll/Resources/election_data.csv')

# print(csvreader)	
tot_vote_cnt = 0
pct_win = float
can_vote_cnt = 0
can_vote_cnt1 = 0
can_vote_cnt2 = 0
can_vote_cnt3 = 0
win_nm = string
line_cnt = 0
can_cnt = 0
line_cnt2 = 0
pct_vote1 = 0.000
pct_vote2 = 0.000
pct_vote3 = 0.000
can_name = string
can_name1 = string
can_name2 = string
can_name3 = string

with open("./Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile,  delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        tot_vote_cnt = sum(1 for row[0] in csvreader)+1


with open("./Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile,  delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
       
    for row in csvreader:
        
        if row[2] == "Charles Casper Stockham":
           can_name1 = row[2]
           can_vote_cnt1 = can_vote_cnt1 + 1
           line_cnt += 1
      
        
        if row[2] == "Diana DeGette":
           can_name2 = row[2]
           can_vote_cnt2 = can_vote_cnt2 + 1
           line_cnt += 1
        
        if row[2] == "Raymon Anthony Doane":
            can_name3 = row[2]
            can_vote_cnt3 = can_vote_cnt3 + 1
            line_cnt = 1  
pct_vote1 = (can_vote_cnt1/tot_vote_cnt) * 100
pct_vote2 = (can_vote_cnt2/tot_vote_cnt)* 100
pct_vote3 = (can_vote_cnt3/tot_vote_cnt)* 100


if can_vote_cnt1 > can_vote_cnt2:
   win_nm = "Winner: " + (can_name1)
elif can_vote_cnt2 > can_vote_cnt3:
    win_nm = "Winner: " + ( can_name2)
else: 
    win_nm ="Winner: " + (can_name3)


print("Election Results")
print("                                                                      ")
print("-----------------------------------------------------------------------------")
print("                                                                      ")
print("Total Votes: " + str(tot_vote_cnt))
print("                                                                      ")
print("-----------------------------------------------------------------------------")
print("                                                                      ")
print(str(can_name1)+": " + str("%.3f" % pct_vote1)+ "%  (" + str(can_vote_cnt1) + ")")
print("                                                                      ")
print(str(can_name2)+": " +str("%.3f" %pct_vote2)+ "%  (" + str(can_vote_cnt2)+ ")")
print("                                                                     ")
print(str(can_name3)+": " +str("%.3f" %pct_vote3)+ "%   (" + str(can_vote_cnt3)+ ")")
print("                                                                      ")
print("-----------------------------------------------------------------------------")
print("                                                                      ")
print("Winner: " + win_nm)
print("                                                                      ")
print("------------------------------------------------------------------------------")

output_path = pathlib.Path("C:/users/shara/PythonStuff/python-challenge/PyPoll/analysis/PyPoll_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
f = open(output_path, "w")

f.writelines("\n")
f.writelines(" Election Results \n")
f.writelines("\n")
f.writelines("-------------------------------------------------------\n")
f.writelines("\n")
f.writelines("Total Votes: " + str(tot_vote_cnt) + "\n")
f.writelines("\n")
f.writelines("----------------------------------------------------------- \n")
f.writelines("\n")
f.writelines(str(can_name1)+": " +str("%.3f" % pct_vote1)+ "%  (" + str(can_vote_cnt1)+  ") \n")
f.writelines("\n")
f.writelines(str(can_name2)+": " +str("%.3f" % pct_vote2)+ "%  (" + str(can_vote_cnt2)+ ")  \n")
f.writelines("\n")
f.writelines(str(can_name3)+": " +str("%.3f" % pct_vote3)+ "%  (" + str(can_vote_cnt3)+ ")  \n")
f.writelines("\n")
f.writelines("----------------------------------------------------------- \n")
f.writelines("\n")
f.writelines("Winner: " + win_nm + "\n")
f.writelines("\n")
f.writelines("----------------------------------------------------------- \n")
f.close()


