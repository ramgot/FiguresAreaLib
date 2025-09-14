from abc import ABC, abstractmethod

class Figure(ABC):
  @abstractmethod
  def area(self):
    pass

  def input_params_check(self, *args):
    for elem in args:
      if type(elem) not in (int, float):
        print(f"Print Us: ", type(elem))
        return 1
      if (elem <= 0):
        return 2
    return 0