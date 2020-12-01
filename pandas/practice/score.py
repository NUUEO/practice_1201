import pandas as pd

data = pd.Series(dtype='float64')
while True:
    name = str(input('請輸入姓名 = '))
    if name == 'stop':
        break
    score = float(input('請輸入成績 = '))
    df = pd.Series(score,index=[name])
    data = pd.concat([data,df], axis=0)
print(data)

data.to_csv('DATA.csv',encoding='utf-8')