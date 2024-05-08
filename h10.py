
a=[16,17,4,3,5,2]
r=[]

n=len(a)

for i in range(len(a)):
    max=a[i]
    max_index=i
    for j in range(max_index+1,len(a),1):
         
         if a[j]>=max:
           # max=a[j]
            r.append(a[j])
         else:
             pass

print(r)         