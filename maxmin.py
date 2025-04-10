def conventional_min_max(arr):
    if not arr:
        return None, None  

    min_element = arr[0]
    max_element = arr[0]

    for num in arr:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num

    return min_element, max_element
def divide_and_conquer_min_max(arr, low, high):
    if low == high:  
        return arr[low], arr[low]

    mid = (low + high) // 2

    left_min, left_max = divide_and_conquer_min_max(arr, low, mid)
    right_min, right_max = divide_and_conquer_min_max(arr, mid + 1, high)

    return min(left_min, right_min), max(left_max, right_max)

def find_min_max(arr):
    if not arr:
        return None, None
    return divide_and_conquer_min_max(arr, 0, len(arr) - 1)

arr = [3, 1, 5, 7, 2, 9, 8]

min_elem, max_elem = conventional_min_max(arr)
print(f"Conventional Approach - Min: {min_elem}, Max: {max_elem}")


min_elem, max_elem = find_min_max(arr)
print(f"Divide & Conquer Approach - Min: {min_elem}, Max: {max_elem}")