from abc import ABC, abstractmethod
from math import pi


# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self) -> float:
#         """Some documentation"""

#     @abstractmethod
#     def correct_shape(self) -> bool:
#         pass


class Shape:
    def calculate_area(self) -> float:
        raise NotImplementedError

    def is_correct(self) -> bool:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius: int = radius

    def calculate_area(self) -> float:
        return pi * self.radius**2


class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side: int = side

    def calculate_area(self) -> float:
        return self.side**2


class Diamond(Shape):
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def calculate_area(self) -> float:
        return self.a * self.b


class Validator:
    def validate_shape(
        self,
        shape: Shape,
        max_limit: float,
    ) -> Shape:
        if shape.calculate_area() > max_limit:
            raise ValueError("The area is too big")

        # print(shape.is_correct())
        return shape


def main():
    c1 = Circle(radius=12)
    s1 = Square(side=10)
    # d1 = Diamond(a=19, b=12)

    validator = Validator()
    shape1 = validator.validate_shape(c1, 1222)
    shape2 = validator.validate_shape(s1, 1323)
    # shape3 = validator.validate_shape("Hello", 1323)

    print(shape1)
    print(shape2)


main()