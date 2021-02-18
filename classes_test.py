# class is blueprint for creating instances
class Dummy(object):
    a = 90
    b = 80


p = Dummy()
print(p)
print(dir(p))

# __init__ is called when ever an object of the class is constructed
# You can see the first argument to the method is self.
# It is a special variable which points to the current object (like this in C++).
# The object is passed implicitly to every method available in it, but we have to get it explicitly
# in every method while writing the methods
# self is received as first arguement automatically.self is an instance passed automatically
# no need of manual assignments and less code using self and init methods.
# also in methods self is used as instance
# self.first = std1.first


class Student(object):
    """
    Returns a ```Student``` object with the given name, branch and year.

    """

    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year
        print("A student object is created.")

    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)


# gives error if less than 4 arguments are passed.std1 is an instance of class
# name ,branch, year are instance variables or attributes
std1 = Student('Kushal', 'CSE', '2005')
std1.print_details()


# All the values stored in the instance via self are data inside of an instance.
# Each instance of the class can have different values for given attribute (anything we access via .
# is also known as attribute).But, when we define an variable in the class level, that is same across all objects


class Point:
    style = "fun"

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(10, 10)
p2 = Point(100, 100)
for r in [p1, p2]:
    print(f"Object {r} has style value= {r.style}")

Point.style = "work"
for p in [p1, p2]:
    print("Object has style value= {r.style}")

print(f"{p}")


# Repr Method

class Point:
    style = "fun"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("hello init method")

    def __repr__(self):
        return f"<Point x={self.x} y={self.y}>"


p1 = Point(10, 10)
p2 = Point(100, 100)
for p in [p1, p2]:
    print(f"Object {p}")

print(Student.__dict__)
print(std1.__dict__)
