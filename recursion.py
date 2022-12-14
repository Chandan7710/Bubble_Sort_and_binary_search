
'''
Python Recursive Function

A function that called itself inside the function untill the 
condition get satisfied is said to be recursive function and the 
technique of employing the recursive function is called recursion.

'''

'''
Recursive Function to find factorial of a
'''
# Example - 1

def fact(m):
    if m ==1 or m == 0:
        return 1
    else:
        return m * fact(m-1)

print("Factorial of 5 = ", fact(5))
print("Factorial of 0 = ", fact(0))
print("Factorial of 1 = ", fact(1))
print("Factorial of 7 = ", fact(7))
print()

# Example - 2

'''
Recursive Function to find sum of the numbers from 1 to number passed
'''

def sum_upto(n):
    if n == 1:
        return 1
    else:
        return n + sum_upto(n-1)

print("Sum of numbers from 0 to 04 = ", sum_upto(4))
print("Sum of numbers from 0 to 10 = ", sum_upto(10))
print("Sum of numbers from 0 to 25 = ", sum_upto(25))
print("Sum of numbers from 0 to 100 = ", sum_upto(100))
print()


'''
Recursive Function to find sum of the numbers between the range of two numbers passed
'''

# Example - 3

def sum_range(num1, num2):
    if num1 == num2:
        return num2
    else:
        return num1 + sum_range(num1+1, num2)

print("Sum of Numbers from 5, 8 = ", sum_range(5, 8))
print("Sum of Numbers from 10, 20 = ", sum_range(10, 20))
print("Sum of Numbers from 77, 100 = ", sum_range(77, 100))
print("Sum of Numbers from 200, 350 = ", sum_range(200, 350))
print()

'''
Recursive Function to find the index position of the element passed
'''

# Example - 4

# Python 3 program for recursive binary search.
 
# Returns index of x in arr if present, else -1

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the specified range of array
        return -1
 

# Test case : 1
# Test array and the element to find
L1 = [13, 24, 26, 28, 34, 38, 45 ,49, 55, 59, 67, 75, 77, 82, 86, 90, 95]
find1 = 45

# Function call to find the index of the element
result = binary_search(L1, 0, len(L1)-1, find1)
 
if result != -1:
    print("Element is present at index : ", result)
else:
    print("Element is not present in the specified range of array")

# Test case : 2
# Test array and the element to find
L2 = [10, 20, 30, 40, 50, 60]
find2 = 60

# Function call to find the index of the element
result = binary_search(L2, 0, len(L2)-1, find2)
 
if result != -1:
    print("Element is present at index : ", result)
else:
    print("Element is not present in the specified range of array")


# Test case : 3
# Test array and the element to find
L3 = [5, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
find3 = 45

# Function call to find the index of the element
result = binary_search(L3, 0, len(L3)-1, find3)
 
if result != -1:
    print("Element is present at index : ", result)
else:
    print("Element is not present in the specified range of array")
