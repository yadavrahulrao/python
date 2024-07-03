n = int(input(" enter the no. of students : "))
data  = { }
subject = ( ' Physics ' , '  Maths  ' , '  history ' )
for i in range (0 , n):
        name = input("enter the  name of student %d : " % (i + 1))
        marks = []
        for x in subject :
                marks.append(int(input("enter marks of %s : " %x)))
        data[name] = marks
for   x,   y  in  data.items():
        total =  sum(y)
        print("%s  ' s  total  marks %d " %(x,total))
        if total < 120:
                print("%s failed :" %x)
        else :
                print("%s passed :" %x)
