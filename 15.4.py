# Write your code here :-)
class Point:
    """Represents a point in 2-D space."""


blank = Point()


blank.x = 3.0
blank.y = 4.0

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(blank)
