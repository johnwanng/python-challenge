import os
import csv

a = [[],[],[]]

def add_to_array(candidateName):
     a[0].append(candidateName)
     a[1].append(1)
     a[2].append(0)

# Path to collect data from the csv file - election_data.csv under the Resources folder
poll_csv = os.path.join('Resources', 'election_data.csv')

totalVotes = 0
candidateFound = 0

# Read the CSV file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row as it contains the column heading
    header = next(csvreader)

     # Loop through the data
    for row in csvreader:
        candidateFound = 0
        totalVotes = totalVotes + 1
        # Check if it is an empty array
        if a[0] == []:
           add_to_array(row[2])
        else:   
            for j in range(len(a[0])):
                if a[0][j] == row[2]:
                    candidateFound = 1      
                    a[1][j] = int(a[1][j]) + 1
            if candidateFound == 0:
               add_to_array(row[2])

#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------


for j in range(len(a[0])):
    #print(round((int(a[1][j])/ totalVotes) * 100,3)) 
    #print(j)    
    a[2][j] = round((int(a[1][j]) / totalVotes) * 100,3)

print(totalVotes)
print(a)

for i in range(len(a[0])):
    print(a[0][i])
    print(a[1][i])
    print(a[2][i])


# Open and write to the output file under the analysis folder 
#fileWriter = open("analysis/Poll_data_result.txt", "w+")
# Write the first row (column headers)
#fileWriter.writelines('Election Results\n')
#fileWriter.writelines('-------------------------\n')
#fileWriter.writelines('Total Votes:' + str(totalVotes) + '\n')
#fileWriter.writelines('-------------------------\n')
#fileWriter.writelines('Total: $' + str(statistics["totalProfitLoss"]) + '\n')
#fileWriter.writelines('Average Change: $' + str(round(statistics["differenceAverage"],2)) + '\n')
#fileWriter.writelines('Greatest Increase in Profits: ' + statistics["greatestIcreaseMonth"] + ' ($' + str(statistics["greatestIncreaseProfitLoss"]) + ')\n')
#fileWriter.writelines('Greatest Decrease in Profits: ' + statistics["greatestDecreaseMonth"] + ' ($' + str(statistics["greatestDecreaseProfitLoss"]) + ')\n')
#fileWriter.close()


