from sparse_matrix import SparseMatrix

def main():
    # Load two sparse matrices from the same sample input for testing
    matrix1 = SparseMatrix('dsa/sparse_matrix/sample_inputs/sample_matrix.txt')
    matrix2 = SparseMatrix('dsa/sparse_matrix/sample_inputs/sample_matrix.txt')

    # Perform addition
    result_add = matrix1.add(matrix2)
    print("Addition Result:")
    for (row, col), value in result_add.data.items():
        print(f"({row}, {col}, {value})")

    # Perform subtraction
    result_subtract = matrix1.subtract(matrix2)
    print("\nSubtraction Result:")
    for (row, col), value in result_subtract.data.items():
        print(f"({row}, {col}, {value})")

    # Perform multiplication
    result_multiply = matrix1.multiply(matrix2)
    print("\nMultiplication Result:")
    for (row, col), value in result_multiply.data.items():
        print(f"({row}, {col}, {value})")

if __name__ == "__main__":
    main()
