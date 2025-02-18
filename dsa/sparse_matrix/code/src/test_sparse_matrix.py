from sparse_matrix import SparseMatrix
import os
import random

def main():
    # Load matrices from the sample_inputs folder
    sample_inputs_folder = 'dsa/sparse_matrix/sample_inputs'
    sample_files = [f for f in os.listdir(sample_inputs_folder) if f.endswith('.txt')]
    if len(sample_files) < 2:
        raise ValueError("Not enough sample input files to proceed.")

    print("Available matrix files:")
    for i, file in enumerate(sample_files):
        print(f"{i+1}. {file}")

    # Find compatible matrix pairs
    compatible_pairs = []
    for i, file1 in enumerate(sample_files):
        matrix1 = SparseMatrix(os.path.join(sample_inputs_folder, file1))
        for j, file2 in enumerate(sample_files[i+1:]):
            matrix2 = SparseMatrix(os.path.join(sample_inputs_folder, file2))
            # Check if matrices are compatible for at least one operation
            if (matrix1.numRows == matrix2.numRows and matrix1.numCols == matrix2.numCols) or \
               (matrix1.numCols == matrix2.numRows):
                compatible_pairs.append((file1, file2))
                break
        
    if not compatible_pairs:
        # 
        raise ValueError("No compatible matrix pairs found for operations.")
        
    # Select first compatible pair
    file1, file2 = compatible_pairs[0]
    matrix1 = SparseMatrix(os.path.join(sample_inputs_folder, file1))
    matrix2 = SparseMatrix(os.path.join(sample_inputs_folder, file2))
    print(f"Selected matrices: {file1} and {file2}")


    # Get operation from user
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    try:
        operation = int(input("Enter operation number: "))
    except ValueError:
        raise ValueError("Invalid operation selection. Please enter 1, 2, or 3.")



    try:
        if operation == 1:
            if matrix1.numRows != matrix2.numRows or matrix1.numCols != matrix2.numCols:
                raise ValueError("Matrices must have same dimensions for addition.")
            result = matrix1.add(matrix2)
            print("\nAddition Result:")
        elif operation == 2:
            if matrix1.numRows != matrix2.numRows or matrix1.numCols != matrix2.numCols:
                raise ValueError("Matrices must have same dimensions for subtraction.")
            result = matrix1.subtract(matrix2)
            print("\nSubtraction Result:")
        elif operation == 3:
            if matrix1.numCols != matrix2.numRows:
                raise ValueError("Number of columns in first matrix must equal number of rows in second matrix for multiplication.")
            result = matrix1.multiply(matrix2)
            print("\nMultiplication Result:")
        else:
            raise ValueError("Invalid operation selected.")

        # Print non-zero elements of result
        for (row, col), value in result.data.items():
            print(f"({row}, {col}, {value})")
            
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
