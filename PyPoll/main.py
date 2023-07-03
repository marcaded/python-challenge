from pathlib import Path
in_file = Path("Resources/election_Data.csv")
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
    
    return total, ccs_percentage, dd_percentage, ra_percentage


# def main():
#     in_file = Path("Resources/election_Data.csv")




# #if __name__ == main():
#     main()

print(open_file(in_file))