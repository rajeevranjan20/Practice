#BMI calcuter
w=eval(input("Enter the weight in KG:"))
h=eval(input("Enter the height in Meters:"))
bmi=w/h**2
print(f"The BMI with weight {w} and height {h} :{bmi:.2f}")