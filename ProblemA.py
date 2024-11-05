#A. Given an array A of N integers, write a function missing_int(A) that returns the smallest
#positive integer (greater than 0) that does not occur in A.
#A = [1, 3, 6, 4, 1, 2] should return 5
#A = [1, 2, 3] should return 4
#A = [-1, -1, -1, -5] should return 1
#A = [1, 3, 6, 4, 1, 7, 8, 10] should return 2


# Function for finding missing smallest positive numbers
def missing_int(A):
    i = 1
    while i in A:
        i += 1 # Will loop until it finds the first missing positive number 
    return i



print (missing_int(A = [1, 3, 6, 4, 1, 2]))
print (missing_int(A = [1, 2, 3]))
print (missing_int(A = [-1, -1, -1, -5]))
print (missing_int(A = [1, 3, 6, 4, 1, 7, 8, 10]))