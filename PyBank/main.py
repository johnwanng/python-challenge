import os
import csv

# Statistics dictionary contains all the various analysis outputs and variables used to derive those calculations
statistics = {
    "totalNumberOfMonths":0,
    "totalProfitLoss":0,
    "greatestIcreaseMonth": "",
    "greatestIncreaseProfitLoss": 0,
    "greatestDecreaseMonth": "",
    "greatestDecreaseProfitLoss": 0,
    "differenceAverageProfitLoss":0,
    "difference":0,
    "lastProfitLoss":0,
    "totalProfitLossDifference":0
}


# Path to collect data from the csv file - budget_data.csv under the Resources folder
bank_csv = os.path.join('Resources', 'budget_data.csv')


# Read the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row as it contains the column heading
    header = next(csvreader)

     # Loop through the data
    for row in csvreader:
        # Increment each row except the column header
        statistics["totalNumberOfMonths"] = statistics["totalNumberOfMonths"] + 1

        # Accumulated the value of Profit Losses column
        statistics["totalProfitLoss"] = statistics["totalProfitLoss"] + int(row[1])

        # For the first data row, assign them to the statistics dictionary attributes 
        if statistics["totalNumberOfMonths"] == 1:
           statistics["greatestIcreaseMonth"] = row[0]
           statistics["greatestDecreaseMonth"] = row[0]
           statistics["greatestIncreaseProfitLoss"] = int(row[1])
           statistics["greatestDecreaseProfitLoss"] = int(row[1])
        else:
            # The difference between the current profit loss minus the last or previous profit loss
            statistics["difference"] = int(row[1]) - statistics["lastProfitLoss"] 
            # Accumulate the difference value to the totalProfitLossDifference
            statistics["totalProfitLossDifference"] = statistics["difference"] + statistics["totalProfitLossDifference"]
            # Determine if the difference value is greater than the pevious recorded one
            # If so, assign them to the specifc statistics dictionary attributes
            if statistics["difference"] > statistics["greatestIncreaseProfitLoss"]:
               statistics["greatestIncreaseProfitLoss"] = statistics["difference"]
               statistics["greatestIcreaseMonth"] = row[0]
            # Determine if the difference value is less than the pevious recorded one
            # If so, assign them to the specific statistics dictionary attributes
            if statistics["difference"] < statistics["greatestDecreaseProfitLoss"]:
               statistics["greatestDecreaseProfitLoss"] = statistics["difference"]
               statistics["greatestDecreaseMonth"] = row[0]   

        # Assign the lastProfitLoss value so the difference can be calculated freo the next iteration
        statistics["lastProfitLoss"] = int(row[1])

    # Work out the differenceAverage figure. Need to minus 1 from the total months because the first row there are only 85 differences as the first row is not included.
    statistics["differenceAverage"] = statistics["totalProfitLossDifference"]/(statistics["totalNumberOfMonths"] - 1)

# Function that perform output to file and console
def finalOutput():

    # List contains output lines that need to be output to file and console 
    outputLines = ['Finanical Analysis\n','-------------------------\n',
                'Total Months: ' + str(statistics["totalNumberOfMonths"]) + '\n',
                'Total: $' + str(statistics["totalProfitLoss"]) + '\n',
                'Average Change: $' + str(round(statistics["differenceAverage"],2)) + '\n',
                'Greatest Increase in Profits: ' + statistics["greatestIcreaseMonth"] + ' ($' + str(statistics["greatestIncreaseProfitLoss"]) + ')\n',
                'Greatest Decrease in Profits: ' + statistics["greatestDecreaseMonth"] + ' ($' + str(statistics["greatestDecreaseProfitLoss"]) + ')\n']

    # Open and write to the output file under the analysis folder 
    fileWriter = open("analysis/budget_data_result.txt", "w+")

    # Loop through outputLines list and start writing and displaying them to file and console, respectively
    for lines in range(len(outputLines)):
        fileWriter.writelines(outputLines[lines])
        print(outputLines[lines])
    
    # Close the file    
    fileWriter.close()
 
# Run the finalOutput function
finalOutput()
