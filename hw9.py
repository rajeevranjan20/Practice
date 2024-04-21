#Painting Room
l=eval(input("Length of Room:"))
b=eval(input("Breadth of Room:"))
h=eval(input("Height of Room:"))
ra=l*b+2*h*(l+b)
n=eval(input("No. of Gallon Required per Unit:"))
rg=ra/n
print(f"The amount of paint:{rg:.2f}")