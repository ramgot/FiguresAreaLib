from .Figure import Figure
from typing import Union
from math import sqrt

class Triangle(Figure):
  def validate_sides(self, a, b, c):
    sides = [a, b, c]
    correctness = super().input_params_check(a, b, c)
    if correctness == 1:
      raise TypeError("Некорректные типы данных для сторон треугольника!")
    elif correctness == 2:
      raise ValueError("Стороны треугольника должны быть больше 0!")
    sides_sorted = sorted(sides)
    if sides_sorted[0] + sides_sorted[1] <= sides_sorted[2]:
      raise ValueError("Неравенство треугольника не выолняется!")
    
    return sides
  

  def __init__(self, a: Union[int | float], b: Union[int | float], c: Union[int | float]):
    self.sides = self.validate_sides(a, b, c)
    self.a, self.b, self.c = self.sides
    
  def is_right_triangle(self):
    sorted_sides = sorted(self.sides)
    return sorted_sides[0] ** 2 + sorted_sides[1] ** 2 == sorted_sides[2] ** 2

  @property
  def area(self):
    sorted_sides = sorted(self.sides)
    square = 0
    if self.is_right_triangle():
      square = sorted_sides[0] * sorted_sides[1] / 2
    else:
      p = sum(self.sides) / 2
      square = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    return square