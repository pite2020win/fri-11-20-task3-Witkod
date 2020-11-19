# Matrix.


# Write a class that can represent any 4𝑥4 real matrix.
# Include two functions to calculate the sum and dot product of two matrices.
# Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
# Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction
# - inversion
# - string representation
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
# Delete these comments before commit!
#
# Good luck.

import math
import logging


class Dim_Exception(Exception):
    def __str__(self):
        return f"Matrix dimentions are wrong"


class Matrix:

    dim_amount = 0
    data = []

    def __init__(self, data):
        self.dim_amount = len(data)
        for row in data:
            if len(row) != len(data):
                raise Dim_Exception()
        self.data = data

    @staticmethod
    def create_from_list(*args):
        dim_amount = math.sqrt(len(args))
        if dim_amount % int(dim_amount) != 0:
            raise Dim_Exception()
        dim_amount = int(dim_amount)
        val_nr = 0
        data = []
        for row_nr in range(dim_amount):
            column = []
            for col_nr in range(dim_amount):
                column.append(args[val_nr])
                val_nr += 1
            data.append(column.copy())
        return Matrix(data)

    def __str__(self):
        text = ""
        for row in self.data:
            for col in row:
                text += str(col) + " "
            text += "\n"
        return text

    def __add__(self, second_matrix):
        data = []
        if self.dim_amount != second_matrix.dim_amount:
            raise Dim_Exception()
        # if isinstance()
        for row_nr in range(self.dim_amount):
            data.append(
                [x+y for x, y in zip(self.data[row_nr], second_matrix.data[row_nr])])
        return Matrix(data)

    def __sub__(self, second_matrix):
        data = []
        if self.dim_amount != second_matrix.dim_amount:
            raise Dim_Exception()
        for row_nr in range(self.dim_amount):
            data.append(
                [x-y for x, y in zip(self.data[row_nr], second_matrix.data[row_nr])])
        return Matrix(data)

    def __mul__(self, value):
        data = []
        for row in self.data:
            column = []
            for col in row:
                column.append(col*value)
            data.append(column.copy())
        return Matrix(data)

    def __matmul__(self, second_matrix):
        data_list = [0 for x in range(int(math.pow(self.dim_amount, 2)))]
        data = Matrix.create_from_list(*data_list).data
        if self.dim_amount != second_matrix.dim_amount:
            raise Dim_Exception()
        for i in range(self.dim_amount):
            for j in range(self.dim_amount):
                for k in range(self.dim_amount):
                    data[i][j] += self.data[i][k] + second_matrix.data[k][j]
        return data


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    try:
        matrix1 = Matrix.create_from_list(1, 2, 3, 4)
        matrix2 = Matrix([[5, 6], [7, 8]])

        matrix3 = matrix1 @ matrix2
        print(matrix3)
    except Dim_Exception:
        logging.getLogger().error("Matices have not the same size")
