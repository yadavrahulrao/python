def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrices cannot be multiplied: incompatible dimensions")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):  
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j]
    return result
def print_matrix(matrix):
    for row in matrix:
        print(row)
A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
result = matrix_multiply(A, B)
print("Resultant Matrix:")
print_matrix(result)
