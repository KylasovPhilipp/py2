                      # task 1

class Matrix:
    def __init__(self, input_data):
        self.input = input_data
    def __str__(self):
        return '\n'.join([' '.join([str(element) for element in line]) for line in self.input])
    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with Shape'
                summ_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summ_line]) + '\n'
        else:
            return 'Problems with Shape'
        return answer
matrix_1 = Matrix([[1, 5], [2, 4], [3, 6], [9, 8]])
matrix_2 = Matrix([[5, 3], [8, 21], [12, 3], [11, 22]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)

                        # task 2

from  abc import ABC, abstractclassmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param
   @abstractclassmethod
   def calculate(self):
        pass
class Coat(Clothes):
    @property
    def calculate(self):
        return (self.param / 6.5) + 0.5)
class Suit(Clothes):
    @property
    def calculate(self):
        return ((2 * self.param) + 0.3)
coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)

                    # task 3

class Cell:
    def __init__(self, nums):
        self.nums = nums
    def __str__(self):
        return self.nums
    def __add__(self, other):
        return 'Sum of cell is' + str(self.nums + other.nums)
    def __sub__(self, other):
        return  self.nums - other.nums if self.nums - other.nums > 0
    def __mul__(self, other):
        return 'Multiply of cells is' + str(self.nums * other.nums)
    def __truediv__(self, other):
        return 'Truediv of cells is' + round(self.nums / other.nums)
cell_1 = Cell(25)
cell_2 = Cell(31)
print(cell_1 + cell_2)

