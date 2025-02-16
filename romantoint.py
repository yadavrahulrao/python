class roman_to_integer:
  def __init__(self):
    self.integer = {"I":1 ,"V":5 , "X":10 , "L": 50 , "C":100 , "D": 500 , "M":1000}

  def calculate(self, roman):
    result = 0
    pre = 0
    for c in reversed(roman):
      now = self.integer[c]
      if now< pre :
        result -= now
      else :
        result += now
      pre = now
    return result
convert = roman_to_integer()
roman = "XXIV"
print(convert.calculate(roman))