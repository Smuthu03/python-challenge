## PyBank
import os
import csv
import math
import string
import pathlib
from pathlib import Path

budgetpath = pathlib.Path('C:/users/shara/PythonStuff/python-challenge/PyBank/Resources/budget_data.csv')

# print(csvreader)	
csvpath = pathlib.Path("C:/users/shara/PythonStuff/python-challenge/PyBank/Resources/budget_data.csv")
pl_val = 0.00
pl_cnt = 0
sum_pl = 0
row_val = 0
total_pl = int
avg_chg = 0.00
line_cnt = 0
DT_INC = string
DT_DEC = string
line_cnt1 = 0
line_cnt2 = 0
grt_inc = 1
grt_dec = 0

with open("./Resources/budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile,  delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        row_val = sum(1 for row[0] in csvreader)+1


with open("./Resources/budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile,  delimiter=',')
    csv_header = next(csvreader)

    total_pl = []
    pl_fst = 0
    pl_nxt = 0
    for row in csvreader:
        total_pl = int(row[1])
        pl_val = total_pl + pl_val
        
        if line_cnt == 0:
           pl_nxt = total_pl
           pl_cnt = 0
           pl_fst = pl_nxt
           line_cnt += 1
        elif line_cnt == 1 :
           pl_nxt = total_pl
           pl_cnt = total_pl - pl_fst
           pl_fst = pl_nxt
           sum_pl = sum_pl+pl_cnt
           line_cnt += 1
        else:
            #pl_nxt = pl_cnt
            pl_nxt = pl_fst
            pl_cnt = total_pl - pl_nxt
            pl_fst = total_pl  
            sum_pl = sum_pl+pl_cnt
            line_cnt = 1        
#  to get the greatest increase            
        if  line_cnt1==0 :
             line_cnt1 += 1
        else:
            if grt_inc < pl_cnt:
                DT_INC = row[0]
                grt_inc = pl_cnt

            line_cnt1 += 1
#  to get the greatest decrease
        if  line_cnt2==0 :
             line_cnt2 += 1
        else:
            if grt_dec > pl_cnt:
                DT_DEC = row[0]
                grt_dec = pl_cnt

        line_cnt2 += 1 
    avg_chg = (sum_pl/(row_val-1))

print("Financial Analysis")
print("                                                            ")
print("-----------------------------------------------------------")
print("Total Months: " + str(row_val))
print("                                                            ")
print("Total: $" + str(pl_val))
print("                                                            ")
print("Average Change: " + str("%.2f" % avg_chg))
print("                                                            ")
print("Greatest Increase in Profits: " + DT_INC + " ($"+str(grt_inc)+")" )
print("                                                            ")
print("Greatest Decrease in Profits: " + DT_DEC + " ($"+str(grt_dec)+")")


output_path = pathlib.Path("C:/users/shara/PythonStuff/python-challenge/PyBank/analysis/PyBank_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
f = open(output_path, "w")

f.writelines(" Financial Analysis \n")
f.writelines("\n")
f.writelines("-------------------------------------------------------\n")
f.writelines("\n")
f.writelines(" Total Months:  " + str(row_val) + "\n")
f.writelines("\n")
f.writelines(" Total: $" + str(pl_val) + "\n")
f.writelines("\n")
f.writelines(" Average Change:  " + str(avg_chg) + "\n")
f.writelines("\n")
f.writelines(" Greatest Increase in Profits:  " + DT_INC + " ($"+str(grt_inc)+")"  + "\n")
f.writelines("\n")
f.writelines(" Greatest Decrease in Profits: " + DT_DEC + " ($"+str(grt_dec)+")" + "\n")
f.writelines("\n")
f.close()