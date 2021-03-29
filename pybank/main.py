import os
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


    print(f'Financial Analysis')    
    print(f'------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${ave_change}')
    print(f'Greatest Increase in Profits: {max_month} (${grtst_profit})')
    print(f'Greatest Decrease in Profits: {min_month} (${grtst_loss})')   

    text_output = "Financial Analysis \n----------------------- \n Total Months: {} \n Total: ${} \n Averange Change: {} \n Greatest Increase in Profits: {} (${}) \n Greatest Decrease in Profits: {} (${}) \n".format(months, total, ave_change,max_month, grtst_profit,min_month, grtst_loss)
    # used the above long boy to shorten the output below, otherwise there would be repeating out.write


#the following is to output the result to a text file - output.txt
out = open("C:/Users/bluec/python-challenge/PyBank/analysis/output.txt", "w")
out.write(text_output)
out.close()

#initially wanted to produce output in .write using a function however it is only able to output str not function.
#hence the lengthy repetitive code.
        
