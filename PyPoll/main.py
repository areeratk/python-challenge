import os
import csv

# Path to collect data from the Resources folder
vote_count_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(vote_count_csv, newline="") as csvfile:
    #Split the data on comma
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    csv_header = next(csvfile)
    
    #Initialize variable to hold Date and Profits/Losses values
    total_vote = 0
    candidate_vote = []
    candidate_list = []
             
    # Read through each row of data after the header and loop through the data
    for row in csvreader:
        #Find each candidate's votes
        #Check for a candidate's name
        if row[2] in candidate_list:
            #Add nothing to the candidate_list
            #Add 1 to the candidate_vote for the index name in the candidate_list
            index_I_am_looking_for = candidate_list.index(row[2])
            candidate_vote[index_I_am_looking_for]+=1
        else:
            candidate_list.append(row[2])
            candidate_vote.append(1)
    
    f = open("PyPoll_output.txt","w+")
    print("-------------------")
    f.write("-------------------\n")
    print(f"Election Results")
    f.write(f"Election Results\n")
    print("---------------------------------------")
    f.write("---------------------------------------\n")
    #Find total votes
    total_vote = sum(candidate_vote)
    print(f"Total Votes: {str(total_vote)}")
    f.write(f"Total Votes: {str(total_vote)}\n")
    print("---------------------------------------")   
    f.write("---------------------------------------\n") 
    for x in candidate_list:
        print(x + ":" + "  " + str(round((candidate_vote[candidate_list.index(x)]/total_vote) * 100.000, 3)) + "%" + "  (" + str(candidate_vote[candidate_list.index(x)]) +")" )
        f.write(x + ":" + "  " + str(round((candidate_vote[candidate_list.index(x)]/total_vote) * 100.000, 3)) + "%" + "  (" + str(candidate_vote[candidate_list.index(x)]) +")\n" )
        if max(candidate_vote) == candidate_vote[candidate_list.index(x)]:
            y = x
    print("---------------------------------------")
    f.write("---------------------------------------\n")
    print(f"Winner: {str(y)}")
    f.write(f"Winner: {str(y)}\n")
    print("---------------------------------------")
    f.write("---------------------------------------\n")
    
