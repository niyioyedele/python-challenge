# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))
Month_count = 0
Total_Profit = 0
Monthly_Change = 0
Greatest_Monthly_Change = [" ",0]
Least_Monthly_Change =[" ",9999999999999999999 ] 
month_change= []

net_change = []

# Method 2: Improved Reading using CSV module

with open(csvpath) as csv_file:
    csvreader = csv.reader(csv_file,delimiter = ',')

    headerline = next(csvreader)

    row1 = next(csvreader)

    Month_count += 1
    Total_Profit +=int(row1[1])

       
    Previous = int(row1[1])
    
    
    


    for row in csvreader:
        Month_count += 1

        Total_Profit += int(row[1])

        

        Monthly_Change = int(row[1]) - Previous

        Previous = int(row[1])

        net_change += [Monthly_Change]
        month_change += [row[0]]

        

        

        if Monthly_Change > Greatest_Monthly_Change[1]:
            Greatest_Monthly_Change[0] = row[0]                    

            Greatest_Monthly_Change = Monthly_Change

        if Monthly_Change < Least_Monthly_Change[1]:
            
            Least_Monthly_Change[0] = row[0]
         
            Least_Monthly_Change = Monthly_Change
        

Ave_Month_Change = sum(net_change)/len(net_change)      

    


print(Month_count)

print(Total_Profit)

print(Ave_Month_Change)

print(Greatest_Monthly_Change)

print(Least_Monthly_Change)

               
    

