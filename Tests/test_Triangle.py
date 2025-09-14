import pytest
from ..Figures.Triangle import Triangle
from math import pi, isclose
class TestTriangle:
  def test_area_calculation_for_usual_triangle_with_sides_6_4_4(self):
    triangle = Triangle(6, 4, 4)
    expected_area = 7.937253933194
    assert isclose(triangle.area, expected_area)
  
  def test_area_calculation_for_right_triangle_with_sides_10_8_6(self):
    triangle = Triangle(10, 8, 6)
    expected_area = 24
    assert isclose(triangle.area, expected_area)

  def test_create_triangle_that_does_not_satisfy_the_triangle_inequality(self):
    with pytest.raises(ValueError):
      triangle = Triangle(1, 2, 3)
  
  def test_create_triangle_with_incorrect_input_params(self):
    with pytest.raises(TypeError):
      circle = Triangle(3, 5, "Hello!")

  def test_create_triangle_with_negative_side(self):
    with pytest.raises(ValueError):
      circle = Triangle(-1, 2, 3)
  
  def test_create_triangle_with_zero_side(self):
    with pytest.raises(ValueError):
      circle = Triangle(1, 1, 0)