#1输入一个含若干自然数的列表，求其平均值，并保留三位小数
data = eval(input('请输入含若干自然数的列表：'))
avg = sum(data) / len(data)
print('%.3f' % avg)
#2输入一个含若干自然数的列表，输出其降序排列后的新列表
print(sorted(data,reverse=True))
#3输入一个含若干自然数的列表,输出一个新列表，新列表中每个元素为原列表中自然数的位数
data=map(str,data)
length = list(map(len,data))
print(length)
#4输入一个含若干数字的列表，输出其绝对值最大的数字
data = eval(input('请输入含若干自然数的列表：'))
print(max(data,key=abs))
#5输入一个含若干整数的列表，输出这些整数的乘积
from operator import mul
from functools import reduce
data = eval(input('请输入含若干整数的列表：'))
print(reduce(mul,data))
#6输入两个包含若干个整数的等长列表，把这两个列表看作两个向量，输出两个向量的内积
a=eval(input('请输入第一个向量：'))
b=eval(input('请输入第二个向量：'))
print(sum(map(mul,a,b)))