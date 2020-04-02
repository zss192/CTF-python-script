#键盘密码解密

chiper='999*666*88*2*777*33*6*999*4*444*777*555*333*777*444*33*66*3*7777'
chiper=chiper.split('*')	#用*隔开

keys=['1','2','3','4','5','6','7','8','9'] 	#有可能是q代表1，w代表2这种，修改这行即可
values=[1,2,3,4,5,6,7,8,9]
dicts=dict(zip(keys,values))

jiugongge=['   ','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
new_dicts=dict(zip(values,jiugongge))

for i in range(len(chiper)):
    temp=dicts.get(chiper[i][0])  #temp=9,6,8,2....
    print(''.join(new_dicts[temp][len(chiper[i])-1]),end='')  #先找到9对应的为wxyz，再根据999的个数取第len-1个