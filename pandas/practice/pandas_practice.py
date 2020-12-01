import pandas as pd

df1 = pd.Series([1,2,3,4],index=['A','B','C','D'])
df2 = pd.Series([55,12,32,94])
# 有無index差異
print(df1)

df = pd.concat([df1,df2],axis=0) # 0與1 方向差異
print(df)

#試做一個可以輸入成績單的資料
#主要科目有 光學 工程數學 微積分 雷射導論 和 Python程式設計
#設計一個程式可供助教分批key各個同學的成績
#最後利用data.to_csv 將資料轉成 csv檔案