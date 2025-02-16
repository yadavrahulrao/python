class integer_to_roman :
  def __init__(self):
    self.integers = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

  def calculate(self, num):
    roman =""
    for x , y in self.integers:
      while num >= x:
        roman += y
        num -= x
    return roman 
  
convert = integer_to_roman()
number = 34
print(convert.calculate(number))