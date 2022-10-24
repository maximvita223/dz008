import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        roster = ''
        for i in self.matrix:
            roster = roster + '\t'.join(map(str, i)) + '\n'
        return roster

    def __add__(self, other):
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


lst_1 = [[1, 2, 4], [3, 4, 5], [5, 6, 6]]
lst_2 = [[11, 21, 41], [31, 41, 51], [51, 61, 61]]
print(Matrix(lst_1)+Matrix(lst_2))
