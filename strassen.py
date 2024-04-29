#Apply Strassen’s Matrix Multiplication strategy for odd dimensional square matrices.
import numpy as np

def pad_matrix(matrix):
    n = len(matrix)
    new_size = n + 1 if n % 2 == 1 else n  # Ensure even size
    padded_matrix = np.pad(matrix, ((0, new_size - n), (0, new_size - n)), mode='constant')
    return padded_matrix

def trim_matrix(matrix, original_size):
    return matrix[:original_size, :original_size]

def strassen_multiply(A, B):
    n = len(A)

    # Base case: If matrices are small, perform regular matrix multiplication
    if n <= THRESHOLD:
        return np.dot(A, B)

    # Pad matrices if necessary to make them even-sized
    if n % 2 == 1:
        A = pad_matrix(A)
        B = pad_matrix(B)

    # Partition matrices
    half_size = n // 2
    A11, A12 = A[:half_size, :half_size], A[:half_size, half_size:]
    A21, A22 = A[half_size:, :half_size], A[half_size:, half_size:]
    B11, B12 = B[:half_size, :half_size], B[:half_size, half_size:]
    B21, B22 = B[half_size:, :half_size], B[half_size:, half_size:]

    # Compute intermediate matrices
    M1 = strassen_multiply(A11 + A22, B11 + B22)
    M2 = strassen_multiply(A21 + A22, B11)
    M3 = strassen_multiply(A11, B12 - B22)
    M4 = strassen_multiply(A22, B21 - B11)
    M5 = strassen_multiply(A11 + A12, B22)
    M6 = strassen_multiply(A21 - A11, B11 + B12)
    M7 = strassen_multiply(A12 - A22, B21 + B22)

    # Combine intermediate matrices to get result
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combine result submatrices into final result
    result = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    # Trim extra rows/columns if matrices were padded
    if n % 2 == 1:
        result = trim_matrix(result, n)

    return result

# Example usage:
THRESHOLD = 64  # Define threshold for base case
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
result = strassen_multiply(A, B)
print(result)