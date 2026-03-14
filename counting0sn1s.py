arr = [1,0,0,1,0,0,1,1,1]

s = 0
max_len = 0
pos = {0:-1}

for i in range(len(arr)):
    
    if arr[i] == 0:
        s -= 1
    else:
        s += 1

    if s in pos:
        max_len = max(max_len, i - pos[s])
    else:
        pos[s] = i

print(max_len)