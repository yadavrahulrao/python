class  school:
        def getstd(self):
                return 12 ;
class  rps (school):
        def getstd(self):
                return 7;
class oxford(school):
        def getstd(self):
                return 8 ; 
a = school()
b = rps()
c = oxford()
print("no. of student in school ",a.getstd());
print("no. of student in rps " , b.getstd());
print(" no. of student in oxford " , c.getstd());
