arr=list(map(int,input("enter elements:").split()))
n=len(arr)
count=0
found=False
for i in range(n):
    count=0
    for j in range(n):
        arr[i]==arr[j]
        count+=1
    if count>n//2:
        print(arr[i])
        found=True
        break
if not found:
    print("-1")