
def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
if __name__ == "__main__":
    elements = [10, 7, 8, 9, 1, 5]
    print("Original Array:", elements)
    sorted_elements = quick_sort(elements)
    print("Sorted Array:", sorted_elements)
