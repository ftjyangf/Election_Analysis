import csv
import os
file_to_save = os.path.join("Resources","election_results.txt")
vote_count = 0

#read the orignal data and count how many votes for each candidates, the percentage somehow can't be wrotten inside the loop,
#so move it out
filename = os.path.join("Resources","election_results.csv")
with open(filename, "r") as data1:
    data_read = csv.reader(data1)
    header = next(data_read)
    unique =[]
    count = {}
    total = 0
    
    for row in data_read:
        
        if not row[2] in unique:
            unique.append(row[2])
            count[row[2]] = 0
        total = total + 1  
        count[row[2]] = count[row[2]] +1
    with open(file_to_save,"w") as txt_file:
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        

# calculate percentage for each candidate, and output by f string
        percentage = {}
        for r in unique:
            percentage[r] = count[r]/total * 100
            results = f"\n{r}:received {percentage[r]:.1f}% of votes({count[r]:,}Votes)\n"       
                    # Save the final vote count to the text file.
            
            txt_file.write(results)

#initate the number
        wining_count = 0
        wining_percentage = 0
        wining_candidate = ""

#find the first valid number and out of loop
        for r in count:
            if count[r]> 0:
                wining_count = count[r]
                wining_percentage = percentage[r]
                wining_candidate = r
                break
#find the biggest number
        for r in count:
            if (count[r] > wining_count) and (percentage[r] > wining_percentage):
                wining_count = count[r]
                wining_percentage = percentage[r]
                wining_candidate = r
#out put the number
        winning_summer = (
            f"---------\n"
            f"Wining_candidata: {wining_candidate}\n"
            f"wining_count: {wining_count:,}\n"
            f"wining_percentage: {wining_percentage:.1f}%\n"
            f"---------\n"
        )
        txt_file.write(winning_summer)

print(winning_summer)

