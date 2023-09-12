import csv
def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here

    f = open('fruits.csv','r')
    dat = csv.reader(f)

    price = []
    for i in list(dat)[1:]:
        price.append(float(i[-1]))
    a = min(price)
    return price.index(a) + 2
print(get_cheapest_fruit_id('fruits.csv'))