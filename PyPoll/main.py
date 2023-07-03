from pathlib import Path

def open_file(fp):
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
