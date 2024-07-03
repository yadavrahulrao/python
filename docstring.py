import math
def longest_side (a,b):
        """  function to find the  length of the longest side of the  right triangle 
        : arg a : side a 
        : arg b : side b 
        : return : side c  """
        return math.sqrt(a*a +b*b)
if    __name__     == ' __main__ ' :
        print(longest_side(4,5))
