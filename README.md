# reto_05_POO_2024-1_JAMB:  **Shape Class: Expanded and Enhanced Part I**
This time Shape Class was divided in Modules, for order and comfort for you and me, and everybody else.

## **Unique Module**
All the _Shape_ Class contained in one Module:

### The "_shape_module_"
Essentially, the code we already know, complete in the packs folder in the Unique Module folder.

For further details about the code, continue to the Multiple Modules section.
```python
from math import things

class Point:
        #...
        #code
        #...

class Line:
        #...
        #code
        #...
        #more code
        #...       

class Shape:
        #...
        #code
        #...

class Triangle(Shape):
        #...
        #code
        #...
        #more code
        #...
        #even more code
        #...

class Equilateral_Triangle(Triangle):
        #...
        #code
        #...
    
class Isosceles_Triangle(Triangle):
        #...
        #code
        #...
    
class Scalene_Triangle(Triangle):
        #...
        #code
        #...

class Rectangle_Triangle(Triangle):
        #...
        #code
        #...
       
class Tetragon(Shape):
        #...
        #code
        #...
        #more code
        #...
        #even more code
        #...

class Square(Tetragon):
        #...
        #code
        #...
        #more code
        #...

class Rectangule(Tetragon):
        #...
        #code
        #...
        #more code
        #...       
```

### The "main"
It's essentially made up of the _Exercise_ Class, included out of mere confusion in previous versions:
```python
import packs.shape_module as shape

def main():
    
    print("\n""\t""Hi there!""\n")
    while True:
        sides = int(input("If you wanna know the components of a Triangle,""\t\t""please write 3""\n""If you wanna know the components of a Quadrilateral,""\t""please write 4""\n""If you wanna end this program,""\t\t\t\t""please write 0""\n"))   
        if sides == 0: break
        if sides == 3:
            #...
            #code
            #...
            #more code
            #...
            #even more code
            #...

            if edges[0] == edges[1] and edges[1] == edges[2]:
                print("\n""\t""The Triangule is Equilateral""\n")
                The_Triangule = shape.Equilateral_Triangle([shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1]), shape.Point(point_C[0], point_C[1])])

            if (edges[0] == edges[1] and edges[1] != edges[2]) or (edges[0] != edges[1] and edges[1] == edges[2]):
                print("\n""\t""The Triangule is Isosceles""\n")
                The_Triangule = shape.Isosceles_Triangle([shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1]), shape.Point(point_C[0], point_C[1])])

            if edges[0] != edges[1] and edges[1] != edges[2]:
                print("\n""\t""The Triangule is Scalene""\n")
                The_Triangule = shape.Scalene_Triangle([shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1]), shape.Point(point_C[0], point_C[1])])  

            print(f"The Triangule Edges are:           {The_Triangule.get_edges()}""\n")
            print(f"The Triangule is Regular:          {The_Triangule.get_is_regular()}""\n")
            print(f"The Triangule Perimeter is:        {The_Triangule.get_perimeter()}""\n")
            print(f"The Triangule Area is:             {The_Triangule.get_area()}""\n")
            print(f"The Triangule Inner Angles are:    {The_Triangule.get_inner_angles()}""\n")
            if "90.0" in The_Triangule.get_inner_angles(): print("The Triangle is Rectangule""\n")

        if sides == 4:
            #...
            #code
            #...
            #more code
            #...
            #even more code
            #...

            if edges[0] == edges[1] and edges[1] == edges[2] and edges[2] == edges[3]:
                    print("\n""\t""The Quadrilateral is a Square""\n")
                    The_Quadrilateral = shape.Square([shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1]), shape.Point(point_C[0], point_C[1]), shape.Point(point_D[0], point_D[1])])

            if edges[0] == edges[1] and edges[1] != edges[2] and edges[2] == edges[3]:
                    print("\n""\t""The Quadrilateral is a Rectangule""\n")
                    The_Quadrilateral = shape.Rectangule([shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1]), shape.Point(point_C[0], point_C[1]), shape.Point(point_D[0], point_D[1])])

            if edges[0] != edges[1] or edges[2] != edges[3]:
                    print("\n""\t""The Quadrilateral is a Trapezoid""\n")
                    The_Quadrilateral = shape.Trapezoid([shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1]), shape.Point(point_C[0], point_C[1]), shape.Point(point_D[0], point_D[1])])  

            print(f"The Quadrilateral Edges are:           {The_Quadrilateral.get_edges()}""\n")
            print(f"The Quadrilateral is Regular:          {The_Quadrilateral.get_is_regular()}""\n")
            print(f"The Quadrilateral Perimeter is:        {The_Quadrilateral.get_perimeter()}""\n")
            print(f"The Quadrilateral Area is:             {The_Quadrilateral.get_area()}""\n")
            print(f"The Quadrilateral Inner Angles are:    {The_Quadrilateral.get_inner_angles()}""\n")           
        print("\t""Have a Nice day, see you again!""\n")

if __name__ == "__main__": 
    main()
```
As you can see, is almost the same, the _Exercise_ Class, unfortunately died, a true shame, thanks for everything.

Now there is an _import_, it's awesome:
```python
import packs.shape_module as shape
```
Because of that, _point_, _line_, _triangle_ and _quadrangle_ objects needs a **_shape_** prefix:
```python
edge_AB = round( shape.Line(shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1])).compute_length(), 3 )

The_Triangule = shape.Scalene_Triangle([shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1]), shape.Point(point_C[0], point_C[1])])

The_Quadrilateral = shape.Rectangule([shape.Point(point_A[0], point_A[1]), shape.Point(point_B[0], point_B[1]), shape.Point(point_C[0], point_C[1]), shape.Point(point_D[0], point_D[1])])
```



## **Multiple Modules**
This time _Point_, _Line_, _Shape_, _Triangle_ and _Quadrangle_ Classes are contained in a module each:

### The _Point_ Class/Module: **_point_cls_**
```python
class Point:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance
```
The grandpa himself.

### The _Line_ Class/Module: **_line_cls_**
```python
from math import asin
from math import degrees

import packages.point_cls as point 

class Line:
    def __init__(self, start: point.Point=0, end: point.Point=0):
        self.start = start
        self.end = end
        self.x_cathetus = self.end.x - self.start.x
        self.y_cathetus = self.end.y - self.start.y

    def compute_length(self):
        hypotenuse = ((self.x_cathetus ** 2) + (self.y_cathetus ** 2)) ** 0.5
        return hypotenuse

    def compute_slope(self):
        hypotenuse = self.compute_length()
        rad = asin(self.y_cathetus / hypotenuse)
        slope = degrees(rad)
        return abs(slope)

    def compute_horizontal_cross(self):
        if self.start.y > 0 and self.end.y > 0:
            return False
        if self.start.y < 0 and self.end.y < 0:
            return False
        else: return True

    def compute_vertical_cross(self):
        if self.start.x > 0 and self.end.x > 0:
            return False
        if self.start.x < 0 and self.end.x < 0:
            return False
        else: return True 
```
Importing from _point_cls_.

### The _Shape_ Class/Module: **_shape_cls_**
```python
import packages.point_cls as point 

class Shape:
    def __init__(self, vertex: list[point.Point]):
        self.vertex = vertex        
```
So sorry I don't know what to do with this poor ugly thing, help.
Importing from _point_cls_.

### The _Triangle_ Class/Module: **_triangle_cls_**
```python
from math import acos
from math import degrees
from math import sqrt

import packages.point_cls as point
import packages.line_cls as line
import packages.shape_cls as shape


class Triangle(shape.Shape):
        #...
        #code
        #...
        #more code
        #...
        #even more code
        #...

class Equilateral(Triangle):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
    def compute_area(self):
        self.area = round( (sqrt(3) / 4) * (self.edge_1 ** 2), 3 )        
        return self.area 
    
class Isosceles(Triangle):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
    def compute_area(self):
        if self.edge_2 == self.edge_3:
            self.__height = sqrt((self.edge_3 ** 2) - ((self.edge_1 / 2) ** 2))
            self.area = round( ((self.edge_1 * self.__height) / 2), 3 )
            return self.area 
        if self.edge_1 == self.edge_2:
            self.__height = sqrt((self.edge_1 ** 2) - ((self.edge_3 / 2) ** 2))
            self.area = round( ((self.edge_3 * self.__height) / 2), 3 )
            return self.area 
    
class Scalene(Triangle):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
    def compute_area(self):
        __semi_perimeter = self.perimeter / 2
        self.area = round(sqrt( __semi_perimeter * (__semi_perimeter - self.edge_1) * (__semi_perimeter - self.edge_2) * (__semi_perimeter - self.edge_3) ), 3)
        return self.area 

class TriRectangle(Triangle):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
    def compute_area(self):
        self.area = round( ((self.edge_1 * self.edge_2) / 2), 3 )
        return self.area
```
Importing from _point_cls_ and _line_cls_.

Now each subclass no more has a `Triangle` prefix:
```python
#before
class Equilateral_Triangle(Triangle):
        #...
        #code
        #...
    
class Isosceles_Triangle(Triangle):
        #...
        #code
        #...
    
class Scalene_Triangle(Triangle):
        #...
        #code
        #...

#after
class Equilateral(Triangle):
        #...
        #code
        #...
    
class Isosceles(Triangle):
        #...
        #code
        #...
    
class Scalene(Triangle):
        #...
        #code
        #...
```

### The _Quadrangle_ Class/Module: **_quadrangle_cls_**
```python
from math import acos
from math import degrees

import packages.point_cls as point
import packages.line_cls as line
import packages.shape_cls as shape
import packages.triangle_cls as triangle 


class Tetragon(shape.Shape):
        #...
        #code
        #...
        #more code
        #...
        #even more code
        #...

class Square(Tetragon):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
        self.edge_1 = line.Line(start=vertex[0], end=vertex[1]).compute_length()
        self.edge_2 = self.edge_1
        self.edge_3 = self.edge_1
        self.edge_4 = self.edge_1

    def compute_perimeter(self):
        self.perimeter = round( (self.edge_1 + self.edge_2 + self.edge_3 + self.edge_4), 3 )
        return self.perimeter

    def compute_area(self):
        self.area = round(self.edge_1 * self.edge_1, 3)
        return self.area
    
    def compute_inner_angles(self):
        __inner_angle_1 = round(360 / 4, 3)
        __inner_angle_2 = __inner_angle_1
        __inner_angle_3 = __inner_angle_1
        __inner_angle_4 = __inner_angle_1
        return [__inner_angle_1, __inner_angle_2, __inner_angle_3, __inner_angle_4]


class Rectangule(Tetragon):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
        self.edge_1 = line.Line(start=vertex[0], end=vertex[1]).compute_length()
        self.edge_2 = line.Line(start=vertex[1], end=vertex[2]).compute_length()
        self.edge_3 = self.edge_1
        self.edge_4 = self.edge_2

    def compute_perimeter(self):
        self.perimeter = round( (self.edge_1 + self.edge_2 + self.edge_3 + self.edge_4), 3 )
        return self.perimeter

    def compute_area(self):
        self.area = round(self.edge_1 * self.edge_2, 3)
        return self.area
    
    def compute_inner_angles(self):
        __inner_angle_1 = round(360 / 4, 3)
        __inner_angle_2 = __inner_angle_1
        __inner_angle_3 = __inner_angle_1
        __inner_angle_4 = __inner_angle_1
        return [__inner_angle_1, __inner_angle_2, __inner_angle_3, __inner_angle_4]
```
Importing from _point_cls_, _line_cls_ and _triangle_cls_.

Now, this bad boy includes a brand new subclass, `Trapezoid`, the quadrilateral with no equal sides:
```python   
class Trapezoid(Tetragon):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
        self.__triangule_1 = triangle.Triangle([vertex[0], vertex[1], vertex[2]])
        self.__triangule_2 = triangle.Triangle([vertex[2], vertex[3], vertex[0]])
        self.edge_1 = line.Line(start=vertex[0], end=vertex[1]).compute_length()
        self.edge_2 = line.Line(start=vertex[1], end=vertex[2]).compute_length()
        self.edge_3 = line.Line(start=vertex[2], end=vertex[3]).compute_length()
        self.edge_4 = line.Line(start=vertex[3], end=vertex[0]).compute_length()

    def compute_perimeter(self):
        self.perimeter = round( (self.edge_1 + self.edge_2 + self.edge_3 + self.edge_4), 3 )
        return self.perimeter

    def compute_area(self):
        self.area = round( (self.__triangule_1.compute_area() + self.__triangule_2.compute_area()), 3 )
        return self.area 
```



### The "main", again
Imports from _point_cls_, _line_cls_, _triangle_cls_ and _quadrangle_cls_.
```python
import packages.point_cls as point
import packages.line_cls as line
import packages.triangle_cls as triangle
import packages.quadrangle_cls as quadrangle 

def main():

    print("\n""\t""Hi there!""\n")
    while True:
        sides = int(input("If you wanna know the components of a Triangle,""\t\t""please write 3""\n""If you wanna know the components of a Quadrilateral,""\t""please write 4""\n""If you wanna exit the program,""\t\t\t\t""please write 0""\n"))   
        if sides == 0: 
            print("\t""Have a Nice day, see you again!""\n")
            break
        
        if sides == 3:
            #...
            #code
            #...
            #more code
            #...
            #even more code
            #...

            if edges[0] == edges[1] and edges[1] == edges[2]:
                print("\n""\t""The Triangule is Equilateral""\n")
                The_Triangule = triangle.Equilateral([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])])

            if (edges[0] == edges[1] and edges[1] != edges[2]) or (edges[0] != edges[1] and edges[1] == edges[2]):
                print("\n""\t""The Triangule is Isosceles""\n")
                The_Triangule = triangle.Isosceles([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])])

            if edges[0] != edges[1] and edges[1] != edges[2]:
                print("\n""\t""The Triangule is Scalene""\n")
                The_Triangule = triangle.Scalene([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])])  

            #...
            #code
            #...
            #more code
            #...
            #even more code
            #...

        if sides == 4:
            #...
            #code
            #...
            #more code
            #...
            #even more code
            #...

            if edges[0] == edges[1] and edges[1] == edges[2] and edges[2] == edges[3]:
                    print("\n""\t""The Quadrilateral is a Square""\n")
                    The_Quadrilateral = quadrangle.Square([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1]), point.Point(point_D[0], point_D[1])])

            if edges[0] == edges[1] and edges[1] != edges[2] and edges[2] == edges[3]:
                    print("\n""\t""The Quadrilateral is a Rectangule""\n")
                    The_Quadrilateral = quadrangle.Rectangule([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1]), point.Point(point_D[0], point_D[1])])

            if edges[0] != edges[1] or edges[2] != edges[3]:
                    print("\n""\t""The Quadrilateral is a Trapezoid""\n")
                    The_Quadrilateral = quadrangle.Trapezoid([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1]), point.Point(point_D[0], point_D[1])])  

            #...
            #code
            #...
            #more code
            #...
            #even more code
            #...           

if __name__ == "__main__": 
    main()
```
Now there are various _import_, it's awesome x2:
```python
import packages.point_cls as point
import packages.line_cls as line
import packages.triangle_cls as triangle
import packages.quadrangle_cls as quadrangle
```
Because of that, _point_, _line_, _triangle_ and _quadrangle_ objects needs a prefix, in this case is the same name, no ideas, sorry:
```python
edge_AB = round( line.Line(point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1])).compute_length(), 3 )

The_Triangule = triangle.Scalene([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])])

The_Quadrilateral = quadrangle.Trapezoid([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1]), point.Point(point_D[0], point_D[1])])
```
No more to say, except for, thanks for reading.
