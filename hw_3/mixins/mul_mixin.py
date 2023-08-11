from hw_3.matrix import Matrix


class HashMixin:
    # returns sum of the sums of the rows squares
    def __hash__(self):
        return sum([sum(map(lambda el: el ** 2, row)) for row in self.data])


class HMatrix(Matrix, HashMixin):
    _hashes = dict()

    def __matmul__(self, other):
        key = (self.__hash__(), other.__hash__())

        # was calculated
        if key in self._hashes:
            return self._hashes[key]

        # wasn't
        result = HMatrix(super().__matmul__(other).data)
        self._hashes[key] = result
        return result
