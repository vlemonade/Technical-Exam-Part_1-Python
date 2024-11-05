#C. Write a rotate(A, k) function which returns a rotated array A, k times; that is, each
#element of A will be shifted to the right k times
#rotate([3, 8, 9, 7, 6], 3) returns [9, 7, 6, 3, 8]
#rotate([0, 0, 0], 1) returns [0, 0, 0]
#rotate([1, 2, 3, 4], 4) returns [1, 2, 3, 4]


# Function to rotate array
def rotate(A, k):
    n = len(A)
    if n == 0:  # If the list is empty, return it as is
        return A
    
    return A[-k:] + A[:-k]  # Return the rotated array



print(rotate([3, 8, 9, 7, 6], 3))  
print(rotate([0, 0, 0], 1))       
print(rotate([1, 2, 3, 4], 4))  
