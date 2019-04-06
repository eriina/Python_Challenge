#import os and csv 
import os 
import csv 

#define file path 
election_data = os.path.join("Resources_1", "election_data.csv")

outfile ="election_results.txt" 

#define variables  
winning_count = 0
winning_candidate = " "
total_votes = 0
candidate = []
candidates_dict = {}

#open file 
with open(election_data) as election_fh:
    reader =  csv.reader(election_fh, delimiter=',')
    header = next(reader) 

    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        #print(candidate_name)
        if candidate_name not in candidate:
            candidate.append(candidate_name)
        #print(candidate)
            candidates_dict[candidate_name] = 0
        candidates_dict [candidate_name] = candidates_dict[candidate_name] + 1


    print(f"Total Votes: {total_votes}")
    for name in candidates_dict:
    # Retrieve vote count and percentage
        votes = candidates_dict.get(name)
        vote_percentage = float(votes) / float(total_votes) * 100

       # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = name

       # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{name}: {vote_percentage:.3f}% ({votes})\n" 
        print(voter_output, end="")
        summary = (
             f"----------------\n"
             f"Winner: {winning_candidate}\n"
            )
    print(summary)

#election_results = os.path.join(“Resources_1”, “election_results.txt”)
    #with open(“election_results.txt”, “w”) as text_file:

    #print to text file
   # print(“Election Results”, file=text_file)
    #print(“----------------------------“, file=text_file)
    #print(f”Total votes: {total_votes} “, file=text_file)
    #print(“----------------------------“, file=text_file)
    #print("voter_output = f"{name}: {vote_percentage:.3f}% ({votes})\n", file=text_file)
    #print(“----------------------------“, file=text_file)
    #print(f”Winner: {winning_candidate}“, file=text_file)
    #print(“----------------------------“, file=text_file)

    #with open(“election_results.txt”, “r”) as text_file2:
    #print(text_file2.read())