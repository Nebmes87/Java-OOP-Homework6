from util.calculator import Calculator
from view.view import Viewer
from data.data import Data


class Controller:
    viewer = Viewer()
    data = Data()

    def __init__(self):
        pass

    def run(self):
        calc = Calculator()

        for i in self.data:
            self.viewer.print(f'Вычисляем: \'{i}\' = {calc.calculate(i)} - контрольное значение: {eval(i)}')