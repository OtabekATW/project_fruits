import csv
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    # data = open('fruits.csv','r').read()
    # rows = data.split('\n')[1:]
    # total = 0
    # for row in rows:
    #     total += float(row.split(',')[1])
    # return total

    f = open('fruits.csv','r')
    dat = csv.reader(f)

    total = 0
    for i in list(dat)[1:]:
        total += float(i[1])

    return total
print(get_total_price('fruits.csv'))
    