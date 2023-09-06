import numpy as np
import logging

logging.basicConfig(filename="log1.txt", encoding="utf-8", level=logging.NOTSET)

logger = logging.getLogger("lg")

class CustomException(Exception):
    pass

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __add__(self, other):
        try:
            if not isinstance(self, Matrix) or not isinstance(other, Matrix):
                logger.error(f'Оба значения должны быть инстансами класса Matrix, получен тип: {type(other)}')
                raise CustomException('Оба значения должны быть инстансами класса Matrix')
            return Matrix(self.matrix + other.matrix)
        except CustomException as e:
            return e

    def __eq__(self, other):
        if not isinstance(self, Matrix) or not isinstance(other, Matrix):
            logger.error(f'Оба значения должны быть инстансами класса Matrix, получен тип: {type(other)}')
            raise CustomException('Оба значения должны быть инстансами класса Matrix')
        return Matrix(self.matrix == other.matrix)
    
    def __mul__(self, other):
        if not isinstance(self, Matrix) or not isinstance(other, Matrix):
            logger.error(f'Оба значения должны быть инстансами класса Matrix, получен тип: {type(other)}')
            raise CustomException('Оба значения должны быть инстансами класса Matrix')
        return Matrix(self.matrix * other.matrix)
    
    def __repr__(self) -> str:
        ret_string = "Матрица:\n"
        for i in self.matrix:
            for j in i:
                ret_string += f"{j} "
            ret_string+="\n"
        return ret_string


logger.info("Program is starting...")

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_class1 = Matrix(matrix1)
m_class2 = Matrix(matrix2)



print(m_class1 + m_class2)
print(m_class1 + 2)
print(m_class1 == m_class2)
# print(m_class1 == 4)
print(m_class1 * m_class2)
# print(m_class1 * 0)
logger.info("Program finished...")