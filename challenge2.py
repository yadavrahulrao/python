# Program to implement Series data structure in Pandas

# import pandas as pd

# # Creating a Series
# data = [10, 20, 30, 40, 50]

# series = pd.Series(data)

# # Display Series
# print("Pandas Series:")
# print(series)

# # Accessing elements
# print("\nFirst Element:")
# print(series[0])

# # Performing operations
# print("\nSeries after adding 5:")
# print(series + 5)

# # Display statistical information
# print("\nMean of Series:")
# print(series.mean())



# Program to implement DataFrame data structure in Pandas

# import pandas as pd

# # Creating a dictionary
# data = {
#     "Name": ["Rahul", "Aman", "Priya", "Neha"],
#     "Age": [20, 21, 19, 22],
#     "Marks": [85, 90, 88, 92]
# }

# # Creating DataFrame
# df = pd.DataFrame(data)

# # Display DataFrame
# print("Pandas DataFrame:")
# print(df)

# # Display column names
# print("\nColumn Names:")
# print(df.columns)

# # Accessing a column
# print("\nName Column:")
# print(df["Name"])

# # Display statistical information
# print("\nAverage Marks:")
# print(df["Marks"].mean())



#pass keyword -- placeholder statement that does nothing , used for empty block ,
#  avoid syntax error  
# def func():
#   pass


#remove duplicates from a list 


# using set()
# num = [1,2,3,4,5,6,4]
# unique = list(set(num))
# print("unique list ",unique)


# x = [3,2,1]
# it = iter(x.pop,2)
# print(next(it))


# x = ["A","B"]
# print(x[True],x[False])

# import numpy as np 

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[7,8,9],[10,11,12]])

# s0 = np.stack((a,b),axis=0)

# d = s0.shape

# print(s0)
# print(d)


# import pandas as pd 
# df = pd.DataFrame({"name":['rahul','rohit'],"marks":[34,23]})

# print(df)

# si = pd.Series([10,20,30,40])
# print(si)


#liner search using for loop 
# num = [10,20,30,40,50]
# tar = 30
# found = False
# for i in num:
#   if i == tar:
#     found = True
#     break

# print("found" if found else "not found")


# x = (i for i in [1,2,0,5])
# all(x)
# print(next(x))


# x = [1,2,3,4]
# for i in x :
#   if i%2 :
#     x.remove(i)
# print(x)
    

# x = map(lambda x: x*2, [1,2,3])
# print(list(zip(x,x)))

# x = iter([1])
# next(x)
# next(x)


# def f():
#   return f
# print(f()()() is f)


# x = [1,2,3]
# print((n := len(x)),n)



# l1 = [1,2,3,4,5,6]
# l2 = [1,3,4,5,7,8]
# c = []
# for i in l1:
#   if i in l2:
#     c.append(i)

# print(i)


n = [1,2,2,3,4,5,6,7,7]
un = [i for i in n if n.count(i) == 1]
print("unique element :",un)