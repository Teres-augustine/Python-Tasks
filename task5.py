print("List of months : January, February, March, April, May, June, July, August, Septemeber, October, November, December");
month_name = input("Input the name of the month : ");
if month_name=='February' :
    print("No. of days = 28/29 days ");
elif month_name in('April','June','September','November') :
    print("No. of days = 30 days ");
elif month_name in('January','March','May','July','August','October','December') :
    print("No. of days = 31 days ");
else :
    print("Wrong Month name");
