# program to calculate  investments . 
# taking input  amount  , rate , period .
amount=float (input("enter amount"))
rate=float(input("enter rate "))
period=int(input("enter year "))

#  initialization of value , year 
value=0
year=1

#  gave condition in while loop 
while year<=period:
    value= amount +(rate * amount)
    print(year,value)
    
    # update
    amount=value
    year = year +1
