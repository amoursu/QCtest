a1, a2, b1, b2 = 1, 2, 3, 4
if a1 < a2 == b1 < b2:
	print "The condition evaluated to True"


def pow(x, y):
	print("{0} ^ {1}".format(x, y))

def cmp(x, y):
	print("{0} ^ {1}".format(x, y))

pow(2,3)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

    # hidden because of attribute with same name
    def area(self, value=None):
        if value == None:
            return self.area
        else:
            self.area = value


r = Rectangle(3, 4)

    # TypeError: int is not callable
print(r.area())