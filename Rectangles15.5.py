# Write your code here :-)
class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """

blank = Point()
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
blank.x = 3.0
blank.y = 4.0

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)

print_point(center)


box.width = box.width + 50
box.height = box.height + 100


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width, box.height)
print(grow_rectangle(box, 50, 100))

print(box.width, box.height)

#Copying

p1 = Point()

p1.x = 3.0

p1.y = 4.0


import copy
p2 = copy.copy(p1)

print_point(p1)

print_point(p2)
