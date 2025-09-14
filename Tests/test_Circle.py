import pytest
from ..Figures.Circle import Circle
from math import pi, isclose
class TestCircle:
  def test_area_calculation_for_radius_10(self):
    circle = Circle(10)
    expected_area = 100 * pi
    assert isclose(circle.area, expected_area)
  
  def test_create_circle_with_incorrect_input_param(self):
    with pytest.raises(TypeError):
      circle = Circle("Radius")

  def test_create_circle_with_negative_radius(self):
    with pytest.raises(ValueError):
      circle = Circle(-1)
  
  def test_create_circle_with_zero_radius(self):
    with pytest.raises(ValueError):
      circle = Circle(0)