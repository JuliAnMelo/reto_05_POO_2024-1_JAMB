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
            point_A = list(map(float, input("\n""Please write the x and y components of the First point:""\t\t").split()))
            point_B = list(map(float, input("\n""Please write the x and y components of the Second point:""\t").split()))
            point_C = list(map(float, input("\n""Please write the x and y components of the Third point:""\t\t").split()))
            edge_AB = round( line.Line(point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1])).compute_length(), 3 ) 
            edge_BC = round( line.Line(point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])).compute_length(), 3 )
            edge_CA = round( line.Line(point.Point(point_C[0], point_C[1]), point.Point(point_A[0], point_A[1])).compute_length(), 3 )
            edges = sorted([edge_AB, edge_BC, edge_CA])

            if edges[0] == edges[1] and edges[1] == edges[2]:
                print("\n""\t""The Triangule is Equilateral""\n")
                The_Triangule = triangle.Equilateral([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])])

            if (edges[0] == edges[1] and edges[1] != edges[2]) or (edges[0] != edges[1] and edges[1] == edges[2]):
                print("\n""\t""The Triangule is Isosceles""\n")
                The_Triangule = triangle.Isosceles([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])])

            if edges[0] != edges[1] and edges[1] != edges[2]:
                print("\n""\t""The Triangule is Scalene""\n")
                The_Triangule = triangle.Scalene([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])])  

            print(f"The Triangule Edges are:           {The_Triangule.get_edges()}""\n")
            print(f"The Triangule is Regular:          {The_Triangule.get_is_regular()}""\n")
            print(f"The Triangule Perimeter is:        {The_Triangule.get_perimeter()}""\n")
            print(f"The Triangule Area is:             {The_Triangule.get_area()}""\n")
            print(f"The Triangule Inner Angles are:    {The_Triangule.get_inner_angles()}""\n")
            if "90.0" in The_Triangule.get_inner_angles(): print("The Triangle is Rectangule""\n")

        if sides == 4:
            point_A = list(map(float, input("\n""Please write the x and y components of the First point:""\t\t").split()))
            point_B = list(map(float, input("\n""Please write the x and y components of the Second point:""\t").split()))
            point_C = list(map(float, input("\n""Please write the x and y components of the Third point:""\t\t").split()))
            point_D = list(map(float, input("\n""Please write the x and y components of the Fourth point:""\t").split()))
            edge_AB = round( line.Line(point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1])).compute_length(), 3 ) 
            edge_BC = round( line.Line(point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1])).compute_length(), 3 )
            edge_CD = round( line.Line(point.Point(point_C[0], point_C[1]), point.Point(point_D[0], point_D[1])).compute_length(), 3 )
            edge_DA = round( line.Line(point.Point(point_D[0], point_D[1]), point.Point(point_A[0], point_A[1])).compute_length(), 3 )
            edges = sorted([edge_AB, edge_BC, edge_CD, edge_DA])

            if edges[0] == edges[1] and edges[1] == edges[2] and edges[2] == edges[3]:
                    print("\n""\t""The Quadrilateral is a Square""\n")
                    The_Quadrilateral = quadrangle.Square([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1]), point.Point(point_D[0], point_D[1])])

            if edges[0] == edges[1] and edges[1] != edges[2] and edges[2] == edges[3]:
                    print("\n""\t""The Quadrilateral is a Rectangule""\n")
                    The_Quadrilateral = quadrangle.Rectangule([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1]), point.Point(point_D[0], point_D[1])])

            if edges[0] != edges[1] or edges[2] != edges[3]:
                    print("\n""\t""The Quadrilateral is a Trapezoid""\n")
                    The_Quadrilateral = quadrangle.Trapezoid([point.Point(point_A[0], point_A[1]), point.Point(point_B[0], point_B[1]), point.Point(point_C[0], point_C[1]), point.Point(point_D[0], point_D[1])])  

            print(f"The Quadrilateral Edges are:           {The_Quadrilateral.get_edges()}""\n")
            print(f"The Quadrilateral is Regular:          {The_Quadrilateral.get_is_regular()}""\n")
            print(f"The Quadrilateral Perimeter is:        {The_Quadrilateral.get_perimeter()}""\n")
            print(f"The Quadrilateral Area is:             {The_Quadrilateral.get_area()}""\n")
            print(f"The Quadrilateral Inner Angles are:    {The_Quadrilateral.get_inner_angles()}""\n")           

if __name__ == "__main__": 
    main()