# Step 1: Import the NumPy library
# NumPy is essential for efficient matrix operations and array handling.
import numpy as np

# Step 2: Define a helper function to input a matrix from the user
# This function asks for the number of rows and columns, then the elements row by row.
def input_matrix(name):
    print(f"\nEnter details for matrix {name}:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    print(f"Enter the elements for {rows}x{cols} matrix (row by row, space-separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Number of elements in row does not match columns. Try again.")
            return input_matrix(name)  # Retry input
        matrix.append(row)
    return np.array(matrix)

# Step 3: Define functions for each matrix operation
# These use NumPy's built-in functions for accuracy and efficiency.

# Addition: Requires two matrices of the same shape
def add_matrices(A, B):
    if A.shape != B.shape:
        return "Error: Matrices must have the same dimensions for addition."
    return A + B

# Subtraction: Requires two matrices of the same shape
def subtract_matrices(A, B):
    if A.shape != B.shape:
        return "Error: Matrices must have the same dimensions for subtraction."
    return A - B

# Multiplication: Performs matrix multiplication (dot product), not element-wise
def multiply_matrices(A, B):
    if A.shape[1] != B.shape[0]:
        return "Error: Number of columns in first matrix must equal number of rows in second matrix."
    return np.dot(A, B)

# Transpose: Flips the matrix along its diagonal
def transpose_matrix(A):
    return A.T

# Determinant: Only for square matrices (rows == columns)
def determinant_matrix(A):
    if A.shape[0] != A.shape[1]:
        return "Error: Matrix must be square (same number of rows and columns) for determinant."
    return np.linalg.det(A)

# Step 4: Define a function to display results in a structured format
# Uses NumPy's array printing for clean, readable output.
def display_result(operation, result):
    print(f"\n--- {operation} Result ---")
    if isinstance(result, str):  # If it's an error message
        print(result)
    else:
        print("Matrix:")
        print(result)
        print(f"Shape: {result.shape}")
    print("-" * 30)

# Step 5: Create the main interactive interface
# This is a menu-driven loop that allows users to choose operations and input matrices.
def main():
    print("Welcome to the Matrix Operations Tool!")
    print("Supported operations: Addition, Subtraction, Multiplication, Transpose, Determinant")
    
    while True:
        print("\nMenu:")
        print("1. Add two matrices")
        print("2. Subtract two matrices")
        print("3. Multiply two matrices (matrix multiplication)")
        print("4. Transpose a matrix")
        print("5. Calculate determinant of a matrix")
        print("0. Exit")
        
        choice = input("Choose an option (0-5): ").strip()
        
        if choice == '0':
            print("Exiting the tool. Goodbye!")
            break
        
        elif choice in ['1', '2', '3']:
            # Operations requiring two matrices
            A = input_matrix("A")
            B = input_matrix("B")
            if choice == '1':
                result = add_matrices(A, B)
                display_result("Addition (A + B)", result)
            elif choice == '2':
                result = subtract_matrices(A, B)
                display_result("Subtraction (A - B)", result)
            elif choice == '3':
                result = multiply_matrices(A, B)
                display_result("Multiplication (A * B)", result)
        
        elif choice == '4':
            # Transpose requires one matrix
            A = input_matrix("A")
            result = transpose_matrix(A)
            display_result("Transpose of A", result)
        
        elif choice == '5':
            # Determinant requires one square matrix
            A = input_matrix("A")
            result = determinant_matrix(A)
            display_result("Determinant of A", result)
        
        else:
            print("Invalid choice. Please select 0-5.")

# Step 6: Run the main function to start the tool
if __name__ == "__main__":
    main()