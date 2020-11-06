#Matrix. 


#Write a class that can represent any 4𝑥4 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
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
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

class Matrixx:
  def __init__(self, row1, row2):
    self.row1 = [row1[0], row1[1]]
    self.row2 = [row2[0], row2[1]]

  def summary(self, matrix):  
    for i in range(self.row1):
      self.row1[i] += matrix.row1[i]
    for i in range(self.row2):
      self.row1[2] += matrix.row1[2] 

  def dot(self):
    pass

  def substraction(self):
    pass

  def invertion(self):
    pass

  def __str__(self):
    print("[")
    for value in row1:
      print("[{value}]".format(value))
    print("]\n[")
    for value in row1:
      print("[{value}]".format(value))
    print("]\n[")

  from 

  if __name__ == "__main__":
    matrix_1 = Matrixx([1,2], [3,4])
    matrix_2 = Matrixx([1,2], [3,4])

    matrix_1.summary(matrix_2)
    print(matrix_1)

