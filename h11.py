a=[12,6,8,5,7,9,3,4,23,14,13]
ec=0
oc=0
for  i in range(len(a)):
    if a[i]%2==0:
        ec=ec+1
    else:
        oc=oc+1
print(ec)
print(oc)            