r,c=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(r)]
max_row=-1
max_count=0
for i in range(r):
    count=matrix[i].count(1)
    if count>max_count:
        max_count=count
        max_row=i

print(max_row)