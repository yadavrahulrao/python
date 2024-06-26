amount=float (input("enter amount"))
rate=float(input("enter rate "))
period=int(input("enter year "))
value=0
year=1
while year<=period:
    value= amount +(rate * amount)
    print(year,value)
    amount=value
    year = year +1
