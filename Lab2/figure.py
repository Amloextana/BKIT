from abc import ABC, abstractmethod


class GeometricFigure(ABC):

    @abstractmethod
    def calculate_square(self):
        pass
