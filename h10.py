
a=[16,17,6,5,2]
r=[]

n=len(a)
max=0
max_index=None

for i in range(n):
    
    if a[i]>max:
         max=a[i]
         max_index=i
    for j in range(max_index+1,len(a)):
         max=a[i]
         if a[j]>max:
           # max=a[j]
              r.append(a[j]) 
              max_index=j   
r.append(a[n-1])
print(r)         