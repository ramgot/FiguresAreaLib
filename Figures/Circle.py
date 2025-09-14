from .Figure import Figure
from math import pi
class Circle(Figure):

  def __init__(self, r):
    correctness = super().input_params_check(r)
    if correctness == 1:
      raise TypeError("Некорректный тип данных для радиуса!")
    elif correctness == 2:
      raise ValueError("Радиус должен быть больше 0!")
    self.r = r
  
  @property
  def area(self):
    return pi * self.r ** 2