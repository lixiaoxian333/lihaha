#倒等腰直角三角形
rows = int(input('输入列数：'))
for i in range(rows,0,-1):
    print('*'*i)
#直角三角形
for i in range(1,10):
    if i%2!=0:
        str=('*'*i)
        print(str)
#正方形
rows = int(input('输入列数：'))
for i in range (0,rows):
    print("*"*rows)
#等腰直角三角形
rows=int(input('输入列数：'))
for i in range(1,rows):
    print('*'*i)
#等腰三角形
row = int(input('please enter a rows'))
for i in range(row):
    for j in range(row - i - 1):
        print(' ',end=' ')
    for k in range(2* i - 1):
            print('*', end=' ')
    print()