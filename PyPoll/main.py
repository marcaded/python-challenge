from pathlib import Path

def open_file(fp):
    ''' Opens file path using variable passed in from main function, counts how many
    votes each candidate has and stores them in the _count variable using slicing, returns
    these count variables'''
    ccs_count = 0
    dd_count = 0
    rad_count = 0
    with open(fp) as fp:
        fp.readline()
        for line in fp:
            line = line.strip().split(',')
            if line[2] == 'Charles Casper Stockham':
                ccs_count +=1
            elif line[2] == 'Diana DeGette':
                dd_count += 1
            else:
                rad_count += 1
    return ccs_count, dd_count, rad_count

def total(countc, countd, countr):
    '''Takes in three agruments for each candidates voter count, adds them all up to get a total vote count, then converts each candidates number of votes into a percentage value using the total votes. Then the if statement finds
    the winner based on the highest percentage of voters for each candidate. Returns the total, each candidates percentage, and the winner as a string.'''
    total = countc+countd+countr
    ccs_percentage = (countc/total)*100
    dd_percentage = (countd/total)*100
    ra_percentage = (countr/total)*100
    winner = ' '
    if ccs_percentage > dd_percentage and ccs_percentage> ra_percentage:
        winner = "Charles Casper Stockham"
        
    elif dd_percentage > ra_percentage and dd_percentage > ccs_percentage:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
    
    return total, ccs_percentage, dd_percentage , ra_percentage, winner
    


def main():
    '''Manages each functions input and output. Passes the election_data.csv file path into the open_file function, takes the return values and 
    passes them in to the total function. Also manages the print statements to the terminal, as well as opening a seperate text file to print the results that file using another path variable defined
    at the top'''
    in_file = Path("Resources/election_data.csv")
    out_file = Path("Analysis/Analysis.txt")
    ccs_count, dd_count, rad_count = open_file(in_file)
    totals, ccs_percentage, dd_percentage , ra_percentage, winner = total(ccs_count, dd_count, rad_count)
    
    
    print("Election Results")
    print('-------------------')
    print("Total Votes: {}".format(totals))
    print('--------------------')
    print("Charles Casper Stockham: {:.3f}% ({})".format(ccs_percentage, ccs_count))
    print("Diana DeGette: {:.3f}% ({})".format(dd_percentage, dd_count))
    print("Raymon Anthony Doane: {:.3f}% ({})".format(ra_percentage, rad_count))
    print("----------------------")
    print("Winner: {}".format(winner))
    
    
    with open(out_file, 'w') as fpath:
        fpath.write("Election Results")
        fpath.write('-------------------')
        fpath.write("Total Votes: {}".format(totals))
        fpath.write('--------------------')
        fpath.write("Charles Casper Stockham: {:.3f}% ({})".format(ccs_percentage, ccs_count))
        fpath.write("Diana DeGette: {:.3f}% ({})".format(dd_percentage, dd_count))
        fpath.write("Raymon Anthony Doane: {:.3f}% ({})".format(ra_percentage, rad_count))
        fpath.write("----------------------")
        fpath.write("Winner: {}".format(winner))






if __name__ == main():
    main()
