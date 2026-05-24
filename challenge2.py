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


x = [3,2,1]
it = iter(x.pop,2)
print(next(it))