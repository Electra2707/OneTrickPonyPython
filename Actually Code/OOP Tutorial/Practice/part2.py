"""Create a Rectangle class that has length and width attributes,
and methods to calculate the perimeter and area of the rectangle.
"""


class Rectangle:
    """Create a Rectangle class that has length and width attributes,
    and methods to calculate the perimeter and area of the rectangle.
    """

    def __init__(self, length, width):
        """The __init__method validates that the length and the width
        inputs are the correct type, and greater than 0

        :param length: Ask for the lenght of the rectangle
        :type length: float or int
        :param width: Ask for the width of the rectangle
        :type width: float or int
        """
        assert isinstance(length, (float, int)
                          ), f"Miss input {length} is {type(length)}"
        assert isinstance(width, (float, int)
                          ), f"Miss input {width} is {type(width)}"
        assert length >= 0, f"Missense in the ({length}) input, should be positive numbers"
        assert width >= 0, f"Missense in the ({width}) input, should be positive numbers"
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        """Calculate the perimeter

        :return: the perimeter
        :rtype: float
        """
        return abs(2*(self.length + self.width))


rectangle1 = Rectangle(5, 3.1)
print(rectangle1.calculate_perimeter())
rectangle2 = Rectangle(40, 50.5)
print(rectangle2.calculate_perimeter())
