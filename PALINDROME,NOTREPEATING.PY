def isPalindrome(num):
    s=str(abs(num))
    return s==s[::-1]
def is_not_repeating(num):
    s=str(abs(num))
    return len(set(s))!=len(s)
L,R=map(int,input("enter elements:").split())
result=[]
for i in range(L,R+1):
    if(i%7==0 and i%5!=0 and not isPalindrome(i) and not is_not_repeating(i)):
        result.append(str(i))
if result:
    print(" ".join(result))
else:
    print("-1")
