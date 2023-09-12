import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f = open('fruits.csv','r')
    dat = csv.reader(f)

    fruits_name = []
    for i in list(dat)[1:]:
        fruits_name.append(i[0])

    return fruits_name
print(get_frutis_name('fruits.csv'))