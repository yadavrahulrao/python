def multi_table(number):
    table = ""
    for i in range(1,11):
        table += f"{i} * {number} = {i*number}\n"
    return table
n = 5
print(multi_table(n))
