n = int(input("enter no. of rows and column :"))
print("enter  matrix a :")
a = []
for i  in  range (0,n) :
        a.append ([int (x)  for x in input( " ") . split (" ")])
print(" enter matrix b :")
b = []
for  i in range(0,n):
        b.append([int(x) for x in input (" ").split(" ")])
c = []
for i in range (0,n):
        c.append([a [i] [j] * b [i] [j]  for j  in range (0, n )])
print(" matrix c ")
for x in c :
        for y in x :
                print(" %5d" %y , end=' ' )
        print( " " )
        
