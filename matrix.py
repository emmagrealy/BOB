class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = []
        self.columns = []

        # Read rows from input string
        inputRows = matrix_string.split("\n")
        for row in inputRows:
            currentRow = row.split(" ")     # separate numbers
            currentRow = list(map(lambda x: int(x), currentRow))    # turn string numbers into integers
            self.rows.append(currentRow)

        # Create columns from rows
        for i in range (0,len(self.rows[0])):   # column index
            currentCol = []
            for j in range (0, len (self.rows)): # row index
                currentCol.append(self.rows[j][i])

            self.columns.append (currentCol)

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return self.columns[index]