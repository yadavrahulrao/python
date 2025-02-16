class student :
  def __init__(self,student_id, student_name, student_class):
    self.student_id = student_id
    self.student_name = student_name
    self.student_class = student_class

  def display(self):
    print("Student Details:")
    print(" ID:", self.student_id)
    print(" NAME:", self.student_name)
    print(" CLASS:", self.student_class)

s = student(23001011049 , 'Rahul' ,'Btech(IT)'  )
s.display()    