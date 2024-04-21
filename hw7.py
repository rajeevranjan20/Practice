#Distance and Time
s1=eval(input("Speed of Car(KM/H):"))
d1=eval(input("Distance Covered by Car(KM):"))
s2=eval(input("Speed of Train(KM/H):"))
d2=eval(input("Distance Covered by Train(KM):"))
s3=eval(input("Speed of Bus(KM/H):"))
d3=eval(input("Distance Covered by Bus(KM):"))
t1=d1/s1
t2=d2/s2
t3=d3/s3
tt=t1+t2+t3
avs=(d1+d2+d3)/tt
print(f"Travel time(Hrs):{tt:.2f}\n Average Speed(KM/H):{avs:.2f}")
