from pathlib import Path

def open_file(fpath):
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
    diff = []
    for i in range(len(lst)):
        try:
            diff.append(lst[i] - lst[i+1])
        except IndexError:
            continue

    avg = -1 * (sum(diff) / len(diff))

    return round(avg, 2)
def profits(lst):
    
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
    increase_day = lst[i+1] 
    decrease_day = lst[j+1] 

    return increase_day, decrease_day






def main():
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
