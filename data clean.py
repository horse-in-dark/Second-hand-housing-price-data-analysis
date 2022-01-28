import pandas as pd  # 导入需要的库

missing_values = ["None", "none", "na", "n/a", "--"]  # 指定空数据类型
df = pd.read_csv('bj.csv', na_values=missing_values, encoding='gbk')
df = df.rename(columns={'简介': 'Introduction', '小区': 'Quarters', '户型': 'HouseType', '面积': 'Area',
                        '关注人数': 'PeopleNumber', '观看次数': 'WatchNumber', '发布时间': 'ReleaseTime',
                        '房价': 'TotalPrice', '单价/平': 'Price', '城区': 'Dist', '经纬度': 'Lotitude'})
print(df.info())  # 查看表格基本信息
df.dropna(inplace=True)  # 修改源数据 DataFrame, 使用 inplace = True 参数:
print(df.info())  # 查看表格基本信息

df.Price = df.Price.map(lambda x: str(x).replace('单价', '').replace('元/平米', ''))
df.Price = df.Price.astype(float)  # astype(float)将数据转成数值型

df.Area = df.Area.map(lambda x: str(x).replace('平米', ''))

df.WatchNumber = df.WatchNumber.map(lambda x: str(x).replace('次带看', '').replace("共", ""))
df.WatchNumber = df.WatchNumber.astype(float)  # astype(float)将数据转成数值型

df.PeopleNumber = df.PeopleNumber.map(lambda x: str(x).replace('人关注', ''))
df.PeopleNumber = df.PeopleNumber.astype(float)  # astype(float)将数据转成数值型

mask = df["HouseType"].str.contains("[\u4e00-\u9fa5]+别墅")  # 使用正则表达式，运用布尔索引
df.loc[mask, 'HouseType'] = df.Area[mask]  # 使用 DafaFrameming.loc[行名,列名] = 值 的方式去赋值,而不是使用DataFrame[][]的形式去赋值

sign = df["Area"].str.contains("[0-9]+室[0-9]+厅")
df.loc[sign, 'Area'] = ((df.TotalPrice * 10000) / df.Price).round(2)

df.Area = df.Area.astype(float)  # astype(float)将数据转成数值型
df.Lotitude = df.Lotitude.astype(str)  # astype(float)将数据转成字符型

print(df.info())

df.to_csv('bj副本.csv', sep=',', index=False, header=True, encoding="gbk")
