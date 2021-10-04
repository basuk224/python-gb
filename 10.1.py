class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y:x + y, r_1, r_2), self.matrix, other.matrix))


m = [[1, 2, 3], [3, 4, 5]]
n = [[6, 7, 8], [9, 10, 11]]

m1 = Matrix(m)

m2 = Matrix(n)

print(m1)
print(m2)
print(m1 + m2)
