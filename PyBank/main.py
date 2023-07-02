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

def average():
    pass

def profits(lst):
    i = 0
    greatest_inc = 0
    greatest_dec = 0

    i = 0
    for i in range(len(lst)):
        try:
            if lst[i] > 0 and lst[i+1] > 0:
                diff = lst[i] - lst[i+1]
                print(diff)
        except IndexError:
            continue
        
        
    
    
    return greatest_inc, greatest_dec
    






def main():
    budget_data_csv = Path("Resources/budget_data.csv")
    months_l, numbers_s, total_profit_loss, total_months = open_file(budget_data_csv)
    greatest_inc, greatest_dec = profits(numbers_s)
    print(greatest_inc, greatest_dec)

main()
