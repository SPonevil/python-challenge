import os
import csv

dates = []
profit = []


total_profit = 0


csvpath = "../Resources/budget_data.csv"

with open(csvpath, mode= 'r', newline =  '') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   next(csvreader)
   for row in csvreader:
       row_list= list(row)

       dates.append(row_list[0])
       profit.append(int(row_list[1]))




print(len(dates))


for x in range(0,len (profit)):
   total_profit = int(profit[x]) + total_profit
print (total_profit)


average_change = total_profit/(len(profit))
print(average_change)


max =0
min=0
for x in range(1, len(profit)-1):
   if int(profit[x]) > max:
       max= int(profit[x])

for x in range(1, len(profit)-1):
   if int(profit[x]) < min:
       min= int(profit[x])

print(max)
print(min)
