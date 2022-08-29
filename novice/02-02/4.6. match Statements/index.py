# point is an (x, y) tuple
def http_nilai(point):
    match point:
        case (0, 0):
             print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
http_nilai((0,3))
# Y=3

class Point:
    x: int
    y: int
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
where_is(Point(80))
# Somewhere else

# def ujian_nasional(point):
# match Point:
#     case []:
#         print("No points")
#     case [Point(x, y)(0, 0)]:
#         print("The origin")
#     case [Point(x, y)(x, y)]:
#         print(f"Single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"Two on the Y axis at {y1}, {y2}")
#     case _:
#         print("Something else")
# where_is(Point(2, 2))
