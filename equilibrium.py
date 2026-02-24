arr=list(map(int,input("enter elements:").split()))
if len(arr)==0:
   print("-1")
   exit()
if len(arr)==1:
   print("0")
   exit()
total=sum(arr)
left_sum=0
found=False
for i in range(len(arr)):
   total=total-arr[i]
   if left_sum==total:
      print(i)
      found=True
      break
   left_sum=left_sum+arr[i]
if not found:
   print("-1")
 