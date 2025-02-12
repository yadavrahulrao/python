def no_boring_zeros(n):
    if n == 0:
        return 0
    elif n< 0:
        return int(str(n).rstrip('0'))
    else :
        return int(str(n).rstrip('0'))
print(no_boring_zeros(1450))
print(no_boring_zeros(960000))
print(no_boring_zeros(1050))
print(no_boring_zeros(-1050))
print(no_boring_zeros(0))
