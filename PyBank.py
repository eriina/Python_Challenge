#import os and csv 
import os 
import csv 
#
#define file path 
budget_data = os.path.join("Resources", "budget_data.csv")

outfile = "summary.txt" 

#define variables for total number of months and total loss/profit
months = 0
net_total = 0.00
average_change = 0

#define variables for determine month for greatest loss and greates increase 
cnt = 0
greatest_increase = 0
greatest_decrease = 0
revchange = 0
currentrev = 0
prevrev = 0
sumrevchange = 0
revchangecnt = 0 

#open file 
with open(budget_data) as budget_fh:
    reader =  csv.reader(budget_fh, delimiter=',')
    header = next(reader) 
    print(header)

    for row in reader:
        cnt = cnt + 1 
        currentrev = float(row["Revenue"])
        currdate = row["Date"]
        sum = sum + currentrev

    for row in reader: 
        net_total = sum (1, 0)

if cnt > 1: 
    revchange = currentrev - prevrev
    sumrevchange = sumrevchange + revchange
    revchangecnt = revchangecnt + 1

if revchange >= 0:
    if revchange > greatest_increase:
        greatest_increase = revchange
        maxrev_date = currdate

elif revchange < 0:
    if revchange < greatest_decrease:
        greatest_decrease = revchange
        maxloss_date = currdate
    prevrev = currentrev

# average of revenue change 
average_change = (sumrevchange / revchange) * 100

print (" ")
print ("Financial Analysis")
print ("Total months: " + str(cnt))
print ("Total Revenue: " + str(sum))
print ("Average Revenue Change $" + str + str(average_change))
print("Greatest Increase in Revenue: " + maxrev_date + " ($" +
              str(greatest_increase) +")" )
print("Greatest Decrease in Revenue: " + maxloss_date + " ($" +
              str(greatest_decrease) +")" )
print(" ")
    
with  open(outfile,'w')  as fhout:
        print("Financial Analysis", file=fhout,end='\n')
        print("----------------------------------------", file=fhout,end='\n')
        print("Total months  : " + str(cnt), file=fhout,end='\n')
        print("Total Revenue : " + str(sum), file=fhout,end='\n')
        print("Average Revenue Change $" + str(average_change),file=fhout,end='\n')
        print("Greatest Increase in Revenue: " + maxrev_date + " ($" +
              str(greatest_increase) +")", file=fhout,end='\n' )
        print("Greatest Decrease in Revenue: " + maxloss_date + " ($" +
              str(greatest_decrease) +")", file=fhout,end='\n' )


