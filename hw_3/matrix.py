class Matrix:
    def __init__(self, array):
        self.matrix_size_check(array)
        self.data = array

    def __add__(self, other):
        self.matrix_size_check(other.data)
        self.matrices_size_check(self.data, other.data)
        return Matrix([list(map(sum, zip(*i)))
                       for i in zip(self.data, other.data)])

    def __mul__(self, other):
        self.matrix_size_check(other.data)
        self.matrices_size_check(self.data, other.data)
        return Matrix([[i * j for i, j in zip(*rs)]
                       for rs in zip(self.data, other.data)])

    def __matmul__(self, other):
        return Matrix([[sum(i * j for i, j in zip(r1, c2))
                        for c2 in zip(*other.data)] for r1 in self.data])

    def __str__(self):
        result = ""
        for r in self.data:
            result += str(r) + "\n"
        return "[\n" + result + "]"

    @staticmethod
    def matrix_size_check(matrix):
        if not all(len(matrix[0]) == len(row) for row in matrix):
            raise ValueError("Incorrect shape")

    @staticmethod
    def matrices_size_check(this, other):
        if not (len(this[0]) == len(other[0]) and len(this) == len(other)):
            raise ValueError("Incorrect shapes")

    @staticmethod
    def check_matrices_size_matmul(this, other):
        if not (len(this[0]) == len(other)):
            raise ValueError("Incorrect shapes")
