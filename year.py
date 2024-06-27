#  program for  getting months  by days .
# taking input as days 
days= int(input("enter days :"))
months = days/30  # division 
days = days % 30    #  modular operator for remainder 
print("Months = %d Days = %d " %(months , days ))


