

def get_recipe_price(list_of_price, optionals=None, **quantity):

    total=0
    if optionals:
        for option in optionals:
            if option in list_of_price:
                list_of_price[option]=0
    for i in quantity.keys():
          total=total+list_of_price[i]*quantity[i]

    return total/100.0


