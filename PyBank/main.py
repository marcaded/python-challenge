from pathlib import Path

def open_file(fpath):
    '''This function opens the file path defined in the main function, splits and seperates the values into two seperate lists. months contains each of the months, and p_l (profi-loss) contains the converted strings to integers
    of the profits and losses. This function returns the months list, the profit losses list, as well as totals of both of the lists'''
    with open(fpath) as fp:
        months = []
        fp.readline()
        numbers_s = []
        for line in fp:
            lines = line.strip().split(',')
            months.append(lines[0])
            numbers_s.append(lines[1])
    
        p_l = [int(number) for number in numbers_s]
        total_profit_loss = sum(p_l)          
        total_months = len(months)
        return months, p_l, total_profit_loss, total_months

def average(lst):
    '''The average function takes in the list of profit losses created by the open file function, it runs through the list finding the difference between each of the months and appends that to the diff list, then returns the 
    rounded average difference '''
    diff = []
    for i in range(len(lst)):
        try:
            diff.append(lst[i] - lst[i+1])
        except IndexError:
            continue

    avg = -1 * (sum(diff) / len(diff))

    return round(avg, 2)
def profits(lst):
    '''The profits function takes in the list of profit losses from the open file function, finds the differences between each of the values, and updates the greatest_inc and greatest_dec values depending on if the iterated 
    difference is greater than or less than that value. This function also updates each of the indexes found based on when that for loop is finished running. profits returns the greatest increase in profits and the greatest
    decrease in profits, as well as both of the indexes'''
    greatest_inc = 0
    greatest_dec = 0
    index = 0
    jndex = 0
    for i in range(len(lst)):
        try:
            diff = lst[i] - lst[i+1]
            if diff > greatest_dec:
                greatest_dec = (diff)
                index = i

            
        except IndexError:
            continue
    for j in range(len(lst)):
        try:
            diff = lst[j] - lst[j+1]
            if diff < greatest_inc:
                greatest_inc = (diff)
                jndex = j
            
        except IndexError:
            continue       
    
    
    return -1 * (greatest_inc), -1 * (greatest_dec), index, jndex
    
def dates(lst, i, j):
    '''Dates takes in the dates list, and both the greatest_increase and greatest_decrease index, and finds each date at the specified index'''
    increase_day = lst[i+1] 
    decrease_day = lst[j+1] 

    return increase_day, decrease_day






def main():
    '''Handles passing in each variable to all of the required functions, as well as prints statements to the terminal and exporting to a seperate txt file path.'''
    budget_data_csv = Path("Resources/budget_data.csv")
    fpath = Path("Analysis/Analysis.txt")
    months_l, numbers_s, total_profit_loss, total_months = open_file(budget_data_csv)
    greatest_inc, greatest_dec, increase_i, decrease_i = profits(numbers_s)
    average_change = average(numbers_s)
    dec_day, inc_day = dates(months_l, increase_i, decrease_i)
    print("Financial Analysis")
    print('----------------------')
    print('Total Months: {}'.format(total_months))
    print("\nTotal: ${}".format(total_profit_loss))
    print("\nAverage Change ${}".format(average_change))
    print("\nGreatest Increase in Profits {} (${})".format(inc_day,greatest_inc ))
    print("\nGreatest Decrease in Profits {} (${})".format(dec_day,greatest_dec ))
    with open(fpath, 'w') as fpath:
        fpath.write("Financial Analysis")
        fpath.write('\n----------------------')
        fpath.write('\nTotal Months: {}'.format(total_months))
        fpath.write("\nTotal: ${}".format(total_profit_loss))
        fpath.write("\nAverage Change ${}".format(average_change))
        fpath.write("\nGreatest Increase in Profits {} (${})".format(inc_day,greatest_inc ))
        fpath.write("\nGreatest Increase in Profits {} (${})".format(inc_day,greatest_inc ))
    

if __name__ == main():
    main()
