# program to print pattern
# pattern 1 
''' n = int(input(" enter no of rows :"))
while n >= 0:
        x  = "*" * n 
        print(x)
        n -= 1  '''

# pattern 2
''' n = int ( input ( " enter rows :"))
i = 1 
while i<=n:
        print("*" * i )
        i += 1  '''

# pattern 3
rows = int ( input (" enter rows :"))
n  = rows 
while n >= 0 :
        x = "* "  * n 
        y = "  "  *  ( rows -  n) 
        print( y + x ) 
        n -= 1 
        
