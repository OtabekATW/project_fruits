def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    # your code here
    rows = data.split('\n')[1:]
    price= []
    for row in rows:
        price.append(row.split(',')[1])
    mx = float(price[0])    
    for exp in price:
        if mx < float(exp):
            mx = float(exp) 
    return mx