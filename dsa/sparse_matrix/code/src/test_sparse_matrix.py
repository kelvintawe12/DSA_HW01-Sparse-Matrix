from sparse_matrix import SparseMatrix
import os
import random
from tabulate import tabulate


def main():
    # Load matrices from the sample_inputs folder
    sample_inputs_folder = 'dsa/sparse_matrix/sample_inputs'
    sample_files = [f for f in os.listdir(sample_inputs_folder) if f.endswith('.txt')]
    if len(sample_files) < 2:
        raise ValueError("Not enough sample input files to proceed.")

    # Display available files in a table
    print("\nAvailable matrix files:")
    table = [[i+1, file] for i, file in enumerate(sample_files)]
    print(tabulate(table, headers=["#", "File Name"], tablefmt="pretty"))


    # Find compatible matrix pairs
    compatible_pairs = {'addition': [], 'subtraction': [], 'multiplication': []}
    for i, file1 in enumerate(sample_files):
        matrix1 = SparseMatrix(os.path.join(sample_inputs_folder, file1))
        for j, file2 in enumerate(sample_files[i+1:]):
            matrix2 = SparseMatrix(os.path.join(sample_inputs_folder, file2))
            # Check if matrices are compatible for addition or subtraction
            if matrix1.numRows == matrix2.numRows and matrix1.numCols == matrix2.numCols:
                compatible_pairs['addition'].append((file1, file2, "Same dimensions"))
                compatible_pairs['subtraction'].append((file1, file2, "Same dimensions"))
            else:
                print(f"\nAddition/Subtraction not possible between {file1} and {file2}:")
                print(f"Matrix 1 dimensions: {matrix1.numRows}x{matrix1.numCols}")
                print(f"Matrix 2 dimensions: {matrix2.numRows}x{matrix2.numCols}")

            # Check if matrices are compatible for multiplication
            if matrix1.numCols == matrix2.numRows:
                compatible_pairs['multiplication'].append((file1, file2, "Columns of first matrix equal rows of second matrix"))
            else:
                print(f"\nMultiplication not possible between {file1} and {file2}:")
                print(f"Matrix 1 columns: {matrix1.numCols}")
                print(f"Matrix 2 rows: {matrix2.numRows}")

    if not any(compatible_pairs.values()):
        raise ValueError("No compatible matrix pairs found for operations.")

    # List compatible pairs for each operation
    # Display compatible pairs in a table
    print("\nCompatible matrix pairs for operations:")
    for operation, pairs in compatible_pairs.items():
        if pairs:
            print(f"\n{operation.capitalize()}:")
            table = [[idx+1, file1, file2, condition] 
                     for idx, (file1, file2, condition) in enumerate(pairs)]
            print(tabulate(table, headers=["#", "Matrix 1", "Matrix 2", "Condition"], 
                          tablefmt="pretty"))


    # Get user selection for operation and matrix pair
    try:
        operation = input("\nEnter operation (addition, subtraction, multiplication): ").strip().lower()
        if operation not in compatible_pairs or not compatible_pairs[operation]:
            raise ValueError("Invalid operation or no compatible pairs for selected operation.")
        
        pair_idx = int(input(f"Enter pair number for {operation}: ")) - 1
        if pair_idx < 0 or pair_idx >= len(compatible_pairs[operation]):
            raise ValueError("Invalid pair selection.")
        
        file1, file2, condition = compatible_pairs[operation][pair_idx]
        matrix1 = SparseMatrix(os.path.join(sample_inputs_folder, file1))
        matrix2 = SparseMatrix(os.path.join(sample_inputs_folder, file2))
        print(f"\nSelected matrices: {file1} and {file2} ({condition})")
    except ValueError as e:
        raise ValueError(f"Selection error: {e}")

    # Get operation from user
    # Display operation menu in a table
    print("\nSelect operation:")
    operations = [
        ["1", "Addition"],
        ["2", "Subtraction"], 
        ["3", "Multiplication"]
    ]
    print(tabulate(operations, headers=["#", "Operation"], tablefmt="pretty"))

    try:
        operation = int(input("Enter operation number: "))
    except ValueError:
        raise ValueError("Invalid operation selection. Please enter 1, 2, or 3.")

    try:
        if operation == 1:
            if matrix1.numRows != matrix2.numRows or matrix1.numCols != matrix2.numCols:
                print(f"\nError: Matrices must have same dimensions for addition.")
                print(f"Matrix 1 dimensions: {matrix1.numRows}x{matrix1.numCols}")
                print(f"Matrix 2 dimensions: {matrix2.numRows}x{matrix2.numCols}")
                raise ValueError("Matrices must have same dimensions for addition.")
            result = matrix1.add(matrix2)
            print("\nAddition Result:")
        elif operation == 2:
            if matrix1.numRows != matrix2.numRows or matrix1.numCols != matrix2.numCols:
                print(f"\nError: Matrices must have same dimensions for subtraction.")
                print(f"Matrix 1 dimensions: {matrix1.numRows}x{matrix1.numCols}")
                print(f"Matrix 2 dimensions: {matrix2.numRows}x{matrix2.numCols}")
                raise ValueError("Matrices must have same dimensions for subtraction.")
            result = matrix1.subtract(matrix2)
            print("\nSubtraction Result:")
        elif operation == 3:
            if matrix1.numCols != matrix2.numRows:
                print(f"\nError: Number of columns in first matrix must equal number of rows in second matrix for multiplication.")
                print(f"Matrix 1 columns: {matrix1.numCols}")
                print(f"Matrix 2 rows: {matrix2.numRows}")
                raise ValueError("Number of columns in first matrix must equal number of rows in second matrix for multiplication.")
            result = matrix1.multiply(matrix2)
            print("\nMultiplication Result:")
        else:
            raise ValueError("Invalid operation selected.")

        # Display result in a table
        print("\nResult Matrix:")
        result_table = [[row, col, value] for (row, col), value in result.data.items()]
        print(tabulate(result_table, headers=["Row", "Column", "Value"], 
                      tablefmt="pretty"))

            
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
