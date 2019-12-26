a=float(input("Input the first number : "));
b=float(input("Input the second number : "));
c=float(input("Input the third number : "));
if a>b:
    if a<c:
        median = a;
    elif b>c:
        median =b;
    else :
        median =c;
else :
    if a>c:
        median =a;
    elif b<c:
        median = b;
    else:
        median =c;
print("The median is : ");
print(median);
