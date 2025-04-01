def evaluate_expression(s: str) -> int:
    s = s.strip()
    return int(eval(s))
print(evaluate_expression("3+2*2")) 
print(evaluate_expression(" 3/2 "))  
print(evaluate_expression(" 3+5 / 2 "))  
