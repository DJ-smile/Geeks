class Figure:
    unit = "cm"

    def __init__(self):
        self._perimeter = 0

    def get_perimeter(self):
        return self._perimeter

    def set_perimeter(self, perimeter):
        self._perimeter = perimeter

    def calculate_area(self):
        raise NotImplementedError("The method should be implemented in the child class")

    def calculate_perimeter(self):
        raise NotImplementedError("The method should be implemented in the child class")

    def info(self):
        raise NotImplementedError("The method should be implemented in the child class")


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self._side_length = side_length
        self.calculate_perimeter()

    def calculate_area(self):
        return self._side_length ** 2

    def calculate_perimeter(self):
        perimeter = 4 * self._side_length
        self.set_perimeter(perimeter)

    def info(self):
        print(f"Square side length: {self._side_length}{self.unit}, perimeter: {self.get_perimeter()}{self.unit}, area: {self.calculate_area()}{self.unit}.")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self._length = length
        self._width = width
        self.calculate_perimeter()

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        perimeter = 2 * (self._length + self._width)
        self.set_perimeter(perimeter)

    def info(self):
        print(f"Rectangle length: {self._length}{self.unit}, width: {self._width}{self.unit}, perimeter: {self.get_perimeter()}{self.unit}, area: {self.calculate_area()}{self.unit}.")


if __name__ == "__main__":
    square1 = Square(5)
    square2 = Square(10)
    rectangle1 = Rectangle(3, 7)
    rectangle2 = Rectangle(4, 8)
    rectangle3 = Rectangle(5, 10)

    figures = [square1, square2, rectangle1, rectangle2, rectangle3]

    for figure in figures:
        figure.info()
