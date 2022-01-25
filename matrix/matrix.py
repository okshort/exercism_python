class Matrix:
    def __init__(self, matrix_string):
        matrix = []
        row_split = "\n"
        rows = matrix_string.split(row_split)
        for element in rows:
            temp = element.split(' ')
            new_temp = list(map(int, temp))
            matrix.append(new_temp)
        self.matrix = matrix

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column = []
        for row in self.matrix:
            column.append(row[index-1])
        return column
