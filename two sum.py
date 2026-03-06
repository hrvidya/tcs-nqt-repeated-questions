arr=list(map(int,input("enter elements:").split()))
target=int(input("enter target:"))
left=0
right=len(arr)-1
found=False
while left<right:
    current_sum=arr[left]+arr[right]
    if current_sum==target:
        print(arr[left],arr[right])
        found=True
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1
if not found:
    print("-1")

