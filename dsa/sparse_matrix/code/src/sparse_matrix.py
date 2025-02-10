class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath is not None:
            self.load_from_file(matrixFilePath)
        elif numRows is not None and numCols is not None:
            self.numRows = numRows
            self.numCols = numCols
            self.data = {}
        else:
            raise ValueError("Either matrixFilePath or numRows and numCols must be provided.")

    def load_from_file(self, matrixFilePath):
        try:
            with open(matrixFilePath, 'r') as file:
                lines = file.readlines()  
                self.numRows = int(lines[0].split('=')[1].strip())  
                self.numCols = int(lines[1].split('=')[1].strip())  
                self.data = {}
                for line in lines[2:]:
                    line = line.strip()
                    if line:
                        row, col, value = map(int, line.strip('()').split(','))
                        self.setElement(row, col, value)
        except Exception as e:
            raise ValueError(f"Error loading file: {e}")

    def getElement(self, currRow, currCol):
        return self.data.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        if value != 0:
            self.data[(currRow, currCol)] = value
        elif (currRow, currCol) in self.data:
            del self.data[(currRow, currCol)]

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for addition.")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (row, col) in set(self.data.keys()).union(other.data.keys()):
            sum_val = self.getElement(row, col) + other.getElement(row, col)
            result.setElement(row, col, sum_val)
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for subtraction.")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (row, col) in set(self.data.keys()).union(other.data.keys()):
            sub_val = self.getElement(row, col) - other.getElement(row, col)
            result.setElement(row, col, sub_val)
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for (row_a, col_a) in self.data:
            for col_b in range(other.numCols):
                val = self.data[(row_a, col_a)] * other.getElement(col_a, col_b)
                if val != 0:
                    result.setElement(row_a, col_b, result.getElement(row_a, col_b) + val)
        return result