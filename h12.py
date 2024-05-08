a=[12,6,8,5,7,9,3,4,23,14,13]
sum=0
r=sorted(a)
n=len(a)
for i in a:
    sum=sum+i
mean=sum/n
print(sum)
print(mean)
print(r)
if n%2==2:
    print(f'median={(r[(n//2)-1] +r[n//2])/2}')
else:
    print(f'median={r[n//2]}')    
