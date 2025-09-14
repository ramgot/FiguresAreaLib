import pytest
from ..Calculators.AreaCalculator import AreaCalculator
from ..Figures.Circle import Circle
from ..Figures.Triangle import Triangle
class TestAreaCalculator:

  def test_circle_area(self):
    circle = Circle(5)
    calc_area = AreaCalculator.area(circle)
    expected_area = circle.area
    assert expected_area == calc_area

  def test_triangle_area(self):
    triangle = Triangle(5, 2, 4)
    calc_area = AreaCalculator.area(triangle)
    expected_area = triangle.area
    assert expected_area == calc_area

