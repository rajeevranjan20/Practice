#pizza party
s=eval(input("No. of Small Size Pizza:"))
cs=eval(input("Cost of Small Pizza:"))
m=eval(input("No. of Medium Size Pizza:"))
cm=eval(input("Cost of Medium Pizza:"))
l=eval(input("No. of Large Size Pizza:"))
cl=eval(input("Cost of Large Pizza:"))
t=eval(input("Cost of Extra Topping:"))
st=s*cs+m*cm+l*cl+t
print(f"Sub Total:{st:.2f}")