data=dict(user='root',passw='123456')
n=0
sum=0
while(n<3):
    lst1=input('用户名：')
    lst2=input('密码:')
    if lst1==data.get('user') and lst2==data.get('passw'):
        print('请选择你要完成的任务:')
        print('*****************')
        print('1 计算1到100的和')
        print('2 输出1到100之间的偶数')
        data2=(int)(input('选择数字：'))
        if data2==1:
            for i in range(1,101):
                sum+=i
            print(sum)
            break
        elif data2==2:
            for i in range(1,101):
                if i%2==0:
                    print(i)
            break
    else:
        n+=1
else:
    print('False')
