#  program to calculate the salary of camera salesman .

# given basic salary , bonus rate , commission rate 
salary = 1500
bonus_rate = 200
commission_rate = 0.02

# taking input as no. of camera sale 
camera = int(input("no . of camera "))
price = int(input("price :"))

# operations to calculate the bonus , commission , total salary  
bonus =  bonus_rate * camera
commission = camera * comission_rate * price 
total =  salary + bonus + commission

print(bonus)
print(commission)
print(total)

