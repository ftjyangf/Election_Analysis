import csv
import os
#file path for read and write files
file_to_read = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Resources","election_results_challenge.txt")
#Step 1:
#Initialize a county list, and candidate_list
counties_list = []
candidate_list = []
#Initialize dictionaries both for counties and candidates, store list of candidate and counties and the numbers based on their name
county_votes = {}
candidate_vote = {}


#Initialize an empty string, and winning_candidate, and the largest turnout storage
county_name = ""
winning_name =""

county_turnout = 0
winning_count = 0
winning_percentage = 0


#read file, store total, count of vote for counties and candidates

total = 0
with open(file_to_read,"r") as election_county:
    election_read = csv.reader(election_county)
    header = next(election_read)
    for row in election_read:
        total = total + 1
        if not row[1] in counties_list:
            counties_list.append(row[1])
            county_votes[row[1]] = 0
        county_votes[row[1]] = county_votes[row[1]] + 1
        if not row[2] in candidate_list:
            candidate_list.append(row[2])
            candidate_vote[row[2]] = 0
        candidate_vote[row[2]] = candidate_vote[row[2]] +1 
        
#initiate variable to store outputs for counties and candidates    
county_result = ""
candidate_result = ""
#calculate percentages
percentage_county = {}
for r in county_votes:
    percentage_county[r] = county_votes[r]/total * 100
    county_result = county_result + (f"countyname:{r}: {percentage_county[r]:.1f}% {county_votes[r]:,}\n")
percentage_candi = {}
for r in candidate_vote:
    percentage_candi[r] = candidate_vote[r]/total * 100
    candidate_result = candidate_result +(f"candidate:{r}: {percentage_candi[r]:.1f}% {candidate_vote[r]:,}\n")

#find the largest number based on the requirement
for r in counties_list:
    if percentage_county[r]> 0:
        county_name = r
        county_turnout = percentage_county[r]
        break
for n in percentage_county:
    if percentage_county[n] > county_turnout:
        county_name = n
        county_turnout = percentage_county[n]

for r in candidate_list:
    if candidate_vote[r]> 0:
        winning_name = r
        winning_percentage = percentage_candi[r]
        winning_vote = candidate_vote[r]
        break
for n in candidate_list:
    if percentage_candi[n] > winning_percentage and candidate_vote[n] > winning_vote:
        winning_name = n
        winning_percentage = percentage_candi[n]
        winning_vote = candidate_vote[n]

#output variable for winning_summer, largest turnout, and election_results
winning_summer = (
            f"-------------------------\n"
            f"Wining_candidata: {winning_name}\n"
            f"wining_count: {winning_vote:,}\n"
            f"wining_percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
largest = (
            f"-------------------------\n"
            f"The largest turnout city: {county_name} {county_turnout:.1f}%\n"
            f"-------------------------\n")
        
election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total:,}\n"
        f"-------------------------\n")
#out put in terminal and write it in txt file
print(election_results,county_result,largest,candidate_result,winning_summer)
allinfo = election_results+county_result+largest+candidate_result+winning_summer
with open(file_to_save, "w") as txt_file:
    txt_file.write(allinfo)
     

