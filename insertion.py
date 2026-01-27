# insertion sort

# arr = [1,3,2,4,6,5]
# n = len(arr)
# for i in range(1,n):
#   temp = arr[i]
#   j = i-1
#   while j>0 and arr[j] > temp :
#     arr[j+1] = arr[j]
#     j -=1
# arr[j+1] = temp

# print(arr)

arr = [1,3,4,2,5,7,6]

# def insertion_sort(arr):
#     # Traverse through 1 to len(arr) (the first element is considered sorted)
for i in range(1, len(arr)):
        # Store the current element to be inserted in a temporary variable (key)
        key = arr[i]
        
        # Initialize j to the index of the element just before the key
        j = i - 1
        
        # Move elements of arr[0...i-1], that are greater than key, 
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key into its correct position in the sorted subarray
        arr[j + 1] = key
# return arr

# # Example Usage:
# my_list = [12, 11, 13, 5, 6]
# print(f"Original list: {my_list}")
# sorted_list = insertion_sort(my_list)
# print(f"Sorted list: {sorted_list}")

print(arr)