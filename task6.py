print("Inpur the lenghts of the sides of the triangle : ");
x = int(input("x : "));
y = int(input("y : "));
z = int(input("z : "));
if x==y==z:
    print("Equilateral Triangle ");
elif x==y or y==z or z==x:
    print("Isosceles Triangle ");
else:
    print("Scalene Triangle ");
