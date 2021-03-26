import os.path
import csv

dirname = os.path.dirname(__file__)
budgetdata_csv = os.path.join(dirname, 'Resources', 'budget_data.csv')

with open(budgetdata_csv, 'r') as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')  # Split the data on commas
    total = 0
    months = 0
    grtst_profit = 0                                #initialise all value on variables
    grtst_loss = 0
    previous_value = 0
    change_list = []

    next(csvfile)
    
    # Loop through the data
    for row in csvreader: 
        
        total = int(row[1]) + total                 #get total of all profit an lost from dataset
        months =  months + 1                        #count the total of months in the row
        change = int(row[1])- int(previous_value)   #to identify the change of values 
        previous_value = row[1]                     
        change_list = change_list + [change]        #to get total of al the changed values
        ave_change = round(sum(change_list)/len(change_list), 2)    # to get average of change

        if int(row[1]) >grtst_profit:               #to get the highest value
            grtst_profit = int(row[1])
            max_month = str(row[0])                 #to get the corresponding month

        elif int(row[1]) < grtst_loss:              #to get the lowest value
            grtst_loss = int(row[1])
            min_month = str(row[0])                 #to get the coresponding month

                                                    # to print the result onto the analysis folder
f = open("C:/Users/bluec/python-challenge/PyBank/analysis/test.txt", "w")
f.write(f'Financial Analysis\n')    
f.write(f'------------------------\n')
f.write(f'Total Months: {months}\n')
f.write(f'Total: ${total}\n')
f.write(f'Average Change: ${ave_change}\n')
f.write(f'Greatest Increase in Profits: {max_month} (${grtst_profit})\n')
f.write(f'Greatest Decrease in Profits: {min_month} (${grtst_loss})\n')    
f.close()    

        
