class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

radius_value = float(input("Enter the radius of the circle: "))

my_circle = Circle(radius_value)

print("Area of the circle:", my_circle.calculate_area())
print("Perimeter of the circle:", my_circle.calculate_perimeter())