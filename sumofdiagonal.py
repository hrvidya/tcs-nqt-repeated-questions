n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n) ]
sum_diagonal=0
for i in range(n):
    sum_diagonal+=matrix[i][i]
print(sum_diagonal)
#in case of row,colums we can use for i in range(min(r,c))