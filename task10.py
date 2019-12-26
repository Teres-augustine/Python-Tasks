class rectangle():
    def __init__(self, l,w):
        self.length=l;
        self.width=w;
    def area(self):
        return self.length*self.width;
a=int(input("Enter length of the rectangle : "));
b=int(input("Enter width of the rectangle : "));
obj=rectangle(a,b)
print("Area of rectangle : ",obj.area());
print();
