
'''

Bubble Sort Algorithm

Sorting the Element of the Array or List Without using sort() function

swapping of the adjacent element until they are not in intended order

=> At first iteration of the loop first min element in the array is moved to the Zeroth index.

=> At second iteration of the loop second min element in the array is moved to the First index.

=> Like wise Loop Continue until sorting the array from lowest to heighest element

'''

def bubble_sort(array):
    print("Before Sorting The Array Elements : ")
    for i in array:
        print(i, end=" ")
    print()

    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    print()

    print("After Sorting The Array Elements : ")
    for i in array:
        print(i, end=" ")
    print()

'''
Calling the function and passing array or list as an parameter
'''
L2 = [24, 35, 65, 77, 41, 21, 14, 41]
bubble_sort(L2)
print()

L3 = [54, 35, 62, 41, 58, 68, 95, 74, 77, 35, 65, 88, 83, 55, 77]
bubble_sort(L3)
print()