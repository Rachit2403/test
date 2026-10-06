def net_price(listed_price, discount=0, tax=0.05):
    return listed_price*(1+tax)*(1-discount)
#print(net_price(250))
print(f"{net_price(564, 0.2, 0.5):.2f}")