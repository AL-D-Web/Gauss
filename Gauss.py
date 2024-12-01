#Copyright2024,All Right Reserved
#Gauss
n = int(input())#输入n*n的矩阵
matrix = []
wei=[]
x=[]
for i in range(n):
    x.append(1);
for i in range(n):
    han=[]
    for j in range(n):
        a=float(input())
        han.append(a)
    matrix.append(han)
for i in range(n):
    a=float(input())
    wei.append(a)
for k in range(0,n-1):#进行n-1次迭代运算
    if matrix[k][k]==0:
        continue
    for i in range(k+1,n):#行号
         c=matrix[i][k]/matrix[k][k]
         for j in range(k,n):#列号
             matrix[i][j]=matrix[i][j]-c*matrix[k][j]
         wei[i]=wei[i]-c*wei[k]#不要忘了x所在列
x[n-1]=wei[n-1]/matrix[n-1][n-1]
print(x[n-1])
for i in range(n-2,-1,-1):
    sum=0
    for j in range(i+1,n):
        sum+=(x[j]*matrix[i][j])
    x[i]=(wei[i]-sum)/matrix[i][i]
for i in range(n):
    print(x[i],end=" ")