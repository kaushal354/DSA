# divide and conquer:-
#1.Min-Max Algorithm using Divide and Conquer

def find_min_max(arr, low, high):
    # If only one element
    if low == high:
        return arr[low], arr[high]
    
    # If two elements, compare directly
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide the array
    mid = (low + high) // 2
    min1, max1 = find_min_max(arr, low, mid)      # Left half
    min2, max2 = find_min_max(arr, mid + 1, high) # Right half

    # Combine results
    return min(min1, min2), max(max1, max2)

# Example Usage
arr = [3, 5, 1, 8, 7, 2, 9]
minimum, maximum = find_min_max(arr, 0, len(arr) - 1)
print(f"Minimum: {minimum}, Maximum: {maximum}")



#2. Strassen's Matrix Multiplication
import numpy as np

def strassen(A, B):
    n = len(A)

    # Base case: 1x1 matrix
    if n == 1:
        return A * B

    # Splitting matrices into quadrants
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Strassen's submatrices
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Compute final quadrants
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combine quadrants
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

# Example Usage
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = strassen(A, B)
print("Resultant Matrix:")
print(C)
