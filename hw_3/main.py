import numpy as np

from hw_3.matrix import Matrix
from hw_3.mixins.mul_mixin import HMatrix
from hw_3.mixins.save_mixin import MMatrix

if __name__ == '__main__':
    np.random.rand(4)

    first_matrix = Matrix(np.random.randint(0, 10, (10, 10)))
    second_matrix = Matrix(np.random.randint(0, 10, (10, 10)))

    with open("artifacts/easy/matrix+.txt", "w") as file:
        file.write((first_matrix + second_matrix).__str__())
    with open("artifacts/easy/matrix*.txt", "w") as file:
        file.write((first_matrix * second_matrix).__str__())
    with open("artifacts/easy/matrix@.txt", "w") as file:
        file.write((first_matrix @ second_matrix).__str__())

    first_matrix = MMatrix(np.random.randint(0, 10, (10, 10)))
    second_matrix = MMatrix(np.random.randint(0, 10, (10, 10)))

    (first_matrix + second_matrix).save_to_file("artifacts/medium/matrix+.txt")
    (first_matrix * second_matrix).save_to_file("artifacts/medium/matrix*.txt")
    (first_matrix @ second_matrix).save_to_file("artifacts/medium/matrix@.txt")

    A = HMatrix([[1, 0], [4, 4]])
    B = HMatrix([[4, 4], [4, 4]])
    C = HMatrix([[3, 4], [2, 2]])
    D = HMatrix([[4, 4], [4, 4]])
    AB = A @ B

    # clean hashes
    C._hashes = dict()

    CD = C @ D

    with open("artifacts/hard/A.txt", "w") as file:
        file.write(A.__str__())
    with open("artifacts/hard/B.txt", "w") as file:
        file.write(B.__str__())
    with open("artifacts/hard/C.txt", "w") as file:
        file.write(C.__str__())
    with open("artifacts/hard/D.txt", "w") as file:
        file.write(D.__str__())

    with open("artifacts/hard/AB.txt", "w") as file:
        file.write(AB.__str__())
    with open("artifacts/hard/CD.txt", "w") as file:
        file.write(CD.__str__())
    with open("artifacts/hard/hash.txt", "w") as file:
        file.write("AB:\n" + (AB.__hash__()).__str__() +
                   "\nCD:\n" + (CD.__hash__()).__str__())
