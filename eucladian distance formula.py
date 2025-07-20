import math as Math
a = int(input("enter the first cordiants on the x axis "))
b  = int(input("enter the second cordiants on the y axis "))
cordinates = (a, b)
#the line below can be writen as distance = (a**2 + b**2)    
distance = (cordinates[0]**2 + cordinates[1]**2)
the_eucladian_distance = Math.sqrt(distance) 
print(the_eucladian_distance)
#this code till here  is  used to calculate between a point and the origin (0,0)
# whtat if we wanted to calculate the distance of two points
# we can use this formula
#distance = Math.sqrt((x2 - x1)**2 + (y2 - y1 )**2)
# we also have to define the second point and ask the user for it 
#a2 = int(input("enter the second cordiants on the x axis "))
#b2 = int(input("enter the second cordiants on the y axis "))
# second_cordiantes = (a2 , b2) 
# repo test