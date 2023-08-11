import numbers

import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class SaveToFileMixin:
    def save_to_file(self, filepath):
        with open(filepath, "w") as file:
            file.write(self.__str__())


class Value:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        result = ""
        for r in self._value:
            result += str(r) + "\n"
        return "[\n" + result + "]"


class MMatrix(NDArrayOperatorsMixin, SaveToFileMixin, Value):
    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MMatrix,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, MMatrix) else x for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, MMatrix) else x for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
