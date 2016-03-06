from math import *

def distance_between(point1, point2):
    """Computes distance between point1 and point2. Points are (x, y) pairs."""
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#prev 2 (3.0933415531887496, 5.413699969452471)
#measurement (4.1979910285832345, 6.47162442378294
#estimate (3.3949752890013785, 5.193629437059418)

print distance_between((3.0933415531887496, 5.413699969452471), (3.3949752890013785, 5.193629437059418))


#prev 1 (1.991599678207975, 4.446082262246948)
#prev 2 (3.216472807162086, 5.3943282199160665)
#measurement (4.29094583946605, 6.36507153289971
#estimate (3.466228597995515, 5.13351895395589)