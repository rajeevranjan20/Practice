#Grocery Shopping
i1=eval(input("Enterbthe quantity of item-1:"))
c1=eval(input("Cost of item-1:"))
i2=eval(input("Enterbthe quantity of item-2:"))
c2=eval(input("Cost of item-2:"))
i3=eval(input("Enterbthe quantity of item-3:"))
c3=eval(input("Cost of item-3:"))
s=i1*c1+i2*c2+i3*c3
tax=s*0.1 #10% of sub total
f=s+tax
print(f"The Subtotal:{s:.2f} and Tax : {tax} \n Final total:{f:.2f}")