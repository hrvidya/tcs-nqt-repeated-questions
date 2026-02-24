#firstnonrepeating character
s=input("enter string:")
if len(s)==0:
    print("-1")
else:
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch in s:
        if freq[ch]==1:
            print(ch)
            break
    else:
        print("-1")
