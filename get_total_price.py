def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    rows = data.split('\n')[1:]
    s = 0
    for row in rows:
        s += float(row.split(',')[1])
    return s