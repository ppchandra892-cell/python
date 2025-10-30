prod_price=[99,199,299,399,499,599,699,799,899]
""" for price in prod_price:
    if price >500:
        break
    print(price) """
i=0
while i<=len(prod_price)-1:
    if prod_price[i]>500:
        break
    print(prod_price[i])
    i=i+1