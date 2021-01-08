import os
import csv

# List containing candidate information.
# First dimension contains names
# Second dimension contsins total number of votes
# Third dimension  contains percentage of votes
candidate = [[],[],[]]

# Function to add new candidate information to the list
def add_to_list(candidateName):
     candidate[0].append(candidateName)
     candidate[1].append(1)
     candidate[2].append(0)

# Path to collect data from the csv file - election_data.csv under the Resources folder
poll_csv = os.path.join('Resources', 'election_data.csv')

# variable to store the total number of votes
totalVotes = 0
# variable to indicate whether the candidate is found or not (0 = not found and 1 = found)
candidateFound = 0

# Read the CSV file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row as it contains the column heading
    header = next(csvreader)

     # Loop through the data
    for row in csvreader:
        # Initialise to candidate flag to not found
        candidateFound = 0
        # Start increment the number of votes
        totalVotes = totalVotes + 1
        # Check if it is an empty list then start adding candidate to list
        if candidate[0] == []:
           add_to_list(row[2])
        else:   
            # Loop through the candidate list
            for j in range(len(candidate[0])):
                # Check to see if the Candidate name is already in the list 
                if candidate[0][j] == row[2]:
                    # Set the Candidate flag to found 
                    candidateFound = 1      
                    # Increment the candidate total vote
                    candidate[1][j] = int(candidate[1][j]) + 1
            # If candidate not found then add new candidate to list        
            if candidateFound == 0:
               add_to_list(row[2])

# Loop through the candidate list and work out its vote perentage and update them accordingly 
for j in range(len(candidate[0])):  
    candidate[2][j] = (int(candidate[1][j]) / totalVotes) * 100


# List contains those header lines that need to be output to file and console 
headerlines = ['Election Results\n','-------------------------\n','Total Votes:' + str(totalVotes) + '\n','-------------------------\n']

# List contains candidate summary informationm 
summaryLines = []
 
# Find index contains the maximum vote
winnerIndex = candidate[1].index(max(candidate[1]))

# List contains the winner lines that need to be output to file and console 
winnerLines = ['-------------------------\n','Winner : ' + candidate[0][winnerIndex] + '\n', '-------------------------\n']
 
# Function that perform output to file and console
def finalOutput():
    # Loop through the candidate list and append their summary information to the summaryLines list and truncate to 3 decimal places
    for i in range(len(candidate[0])):    
        summaryLines.append(candidate[0][i] + ': ' + format(candidate[2][i],'.3f') + '%' + ' (' + str(candidate[1][i]) + ')\n')
    # Open and write to the output file under the analysis folder 
    fileWriter = open("analysis/Poll_data_result.txt", "w+")
 
    # Loop through headerLines list and start writing and displaying them to file and console, respectively
    for lines in range(len(headerlines)):
        fileWriter.writelines(headerlines[lines])
        print(headerlines[lines])

    # Loop through summaryLines list and start writing and displaying them to file and console, respectively
    for lines in range(len(summaryLines)):
        fileWriter.writelines(summaryLines[lines])
        print(summaryLines[lines])

    # Loop through winnerLines list and start writing and displaying them to file and console, respectively
    for lines in range(len(winnerLines)):
        fileWriter.writelines(winnerLines[lines])
        print(winnerLines[lines])
    # Close the file    
    fileWriter.close()
 
# Run the finalOutput function
finalOutput()
