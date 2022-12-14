
'''
Iterative Binary Search Function

It returns index of x in given array arr if present,
else returns -

'''


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
# Test case : 1
# Test array and the element to 

array_1 = [ 2, 3, 4, 10, 40 ]
find_element_1 = 10
 
# Function call
result_1 = binary_search(array_1, find_element_1)
 
if result_1 != -1:
    print(f"Element {find_element_1} is present at index :", result_1)
else:
    print(f"Element {find_element_1} is not present in array")


# Test case : 2
# Test array and the element to

array_2 = [21, 24, 27, 32, 35, 38, 45, 49, 52, 58, 64, 67, 72, 77, 83, 87, 96]
find_element_2 = 77
 
# Function call
result_2 = binary_search(array_2, find_element_2)
 
if result_2 != -1:
    print(f" {find_element_2} Element is present at index :", result_2)
else:
    print(f" {find_element_2} Element is not present in array")
