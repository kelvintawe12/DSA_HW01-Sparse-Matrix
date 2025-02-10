class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath:
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
            print(f"Error opening file: {e}")
            return

    def getElement(self, currRow, currCol):
        return self.data.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        if value != 0:
            self.data[(currRow, currCol)] = value
        elif (currRow, currCol) in self.data:
            del self.data[(currRow, currCol)]

    def add(self, other):
        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.data.items():
            result.setElement(row, col, value + other.getElement(row, col))
        return result

    def subtract(self, other):
        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.data.items():
            result.setElement(row, col, value - other.getElement(row, col))
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
        result = SparseMatrix(self.numRows, other.numCols)
        for (row, col), value in self.data.items():
            for k in range(other.numCols):
                result.setElement(row, k, result.getElement(row, k) + value * other.getElement(col, k))
        return result
