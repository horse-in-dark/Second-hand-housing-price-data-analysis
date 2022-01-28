import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import norm
from scipy import optimize

data = pd.read_csv("bj副本.csv", encoding='gbk')

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

# 整体房价分析
# 输出北京二手房的最高价格、最低价格、平均价格和中位数价格
# price = data['Price']
# max_price = price.max()
# min_price = price.min()
# mean_price = price.mean()
# median_price = price.median()
#
# print("北京市二手房最高价格：%.2f元/平方米" % max_price)
# print("北京市二手房最低价格：%.2f元/平方米" % min_price)
# print("北京市二手房平均价格：%.2f元/平方米" % mean_price)
# print("北京市二手房中位数价格：%.2f元/平方米" % median_price)
# -------------------------#

# 由于变量名重复问题，建议下面的每一大段代码单独运行，防止报错！！！！

# --------------------------#


# 二手房源房源整体特点分析:
# 绘制房源情况柱状图
# 获取各个区域的二手房数量（已排序）
# x = data['Dist'].value_counts().index.tolist()
# y = data['Dist'].value_counts().tolist()
#
# plt.figure(figsize=(8, 7))
# plt.bar(x, y)
# plt.title("北京市各城区房源情况")
# plt.grid(linestyle=":", color="r")
# plt.xticks(rotation=60)
# for a, b in zip(x, y):
#     plt.text(a, b, b, ha='center', va="bottom", fontsize=8)
# plt.savefig("数据分析的那些图/北京市各城区房源情况")
# plt.show()

# # 绘制整体房源面积的频率分布直方图：
# print(data.Area.describe())  # 查看房屋面积的统计信息
#
# fig, axes = plt.subplots()
# sns.histplot(data['Area'], bins=50, kde=False, ax=axes)
# axes.set(xlabel='面积/平米', ylabel='概率密度', title='二手房面积频率分布直方图')
# # 设置直方图的x轴标签、y轴标签以及直方图的标题
# plt.savefig('数据分析的那些图/二手房面积频率分布直方图')  # 保存图片
# plt.show()


# # 各城区二手房均价分析
# df = data.groupby('Dist')
# ave = df['Price'].mean().round(2)
# plt.rcParams['font.sans-serif'] = ['FangSong']
# plt.figure(figsize=(12, 6))
# plt.bar(ave.index, ave.values)
# plt.title('各城区二手房均价')
# plt.xlabel('城区', fontsize=15)
# plt.ylabel('均价', fontsize=15)
# for a, b in zip(ave.index, ave.values):
#     plt.text(a, b, b, ha='center', va="bottom", fontsize=8)
# plt.savefig('数据分析的那些图/各城区二手房均价')
# plt.show()


# # 各城区二手房数量比例饼状图
# areanumber = data["Dist"].groupby(data["Dist"]).count()
# areaname = areanumber.index.values
# plt.figure(figsize=(10, 10))
# plt.pie(areanumber, labels=areaname, autopct='%.1f%%')
# plt.title("各城区二手房数量比例图")
# plt.legend(bbox_to_anchor=(0, 0.6))
# plt.savefig("数据分析的那些图/各城区二手房数量比例饼状图")
# plt.show()

# # 对经纬度数据进行转换，以用于热力图的绘制
# for i in data.Lotitude:
#     lotitude = i.split(',')
#     lng = lotitude[0]
#     lat = lotitude[1]
#     count = "5"
#     out = '{"lng":' + lng + ',"lat":' + lat + ',"count":' + count + '},'
#     print(out)

# # 热门户型均价分析
# housetype = data.groupby('HouseType')
# a = housetype['HouseType'].count().sort_values(ascending=False).head(8)
# b = housetype["Price"].mean()[a.index]
# m = b.index
# n = b.values.astype(int)
# plt.figure(figsize=(10, 6))
# plt.barh(m, n, alpha=0.9, color=['green', 'red', 'blue', 'grey', 'pink', 'yellow', 'black', 'cyan'])
# plt.xlabel("均价", fontsize=15)
# plt.ylabel('户型', fontsize=15)
# plt.title("热门户型均价", fontsize=20)
# for n, m in enumerate(n):
#     plt.text(m + 100, n, str(m) + '元', ha='left')
# plt.savefig("数据分析的那些图/热门户型均价柱形图")
# plt.show()


# 探究影响二手房价格的主要因素有哪些？


# # 绘制各个城区房屋总价的箱线图
# plt.figure(figsize=(20, 10))
# sns.boxplot(x='Dist', y='TotalPrice', data=data)
# plt.xlabel('城区', fontsize=20)
# plt.ylabel('二手房总价', fontsize=20)
# plt.title('北京市各城区二手房总价', size=20)
# plt.savefig("数据分析的那些图/各个城区房屋总价箱线图")
# plt.show()


# # 绘制各个城区房屋单价的箱线图
# plt.figure(figsize=(16, 8))
# sns.boxplot(x='Dist', y='Price', data=data)
# plt.xlabel('城区', fontsize=20)
# plt.ylabel('二手房单价', fontsize=20)
# plt.title('北京市各城区二手房房价', size=20)
# plt.savefig("数据分析的那些图/各个城区房屋单价箱线图")
# plt.show()


# 房屋面积与房价的关系——散点图
# x = data['Area']
# y = data['Price']
# plt.scatter(x, y, s=2.5)
# plt.title("房屋面积对二手房价的影响")
# plt.xlabel("面积", fontsize=15)
# plt.ylabel('单价', fontsize=15)
# plt.savefig('数据分析的那些图/房屋面积与房价的关系——散点图')
# plt.show()

# 全部数据的散点图分布很乱，看不到明显的规律.17个区域内房价应该存在不同的分布规律，因此有必要区分各区进行分析：
# plt.figure(figsize=(10, 8))
# colors = ['red', 'red', 'red', 'red',
#           'blue', 'blue', 'blue', 'blue',
#           'green', 'green', 'green', 'green',
#           'gray', 'gray', 'gray', 'gray', 'gray']
# district = ['昌平', '朝阳', '海淀', '丰台',
#             '燕郊', '大兴', '通州', '西城',
#             '顺义', '东城', '房山', '石景山',
#             '亦庄开发区', '门头沟', '密云', '怀柔', '延庆']
# markers = ['o', 's', 'v', 'x',
#            'o', 's', 'v', 'x',
#            'o', 's', 'v', 'x',
#            'o', 's', 'v', 'x', 'o']
# for i in range(17):
#     x = data.loc[data['Dist'] == district[i]]["Area"]
#     y = data.loc[data["Dist"] == district[i]]['Price']
#     plt.scatter(x, y, c=colors[i], s=20, label=district[i], marker=markers[i])
#
# plt.legend(loc=1, bbox_to_anchor=(1.138, 1.0), fontsize=12)
# plt.title("北京市各城区房屋面积对房价的影响（散点图）")
# plt.xlabel('房屋面积（平方米）', fontsize=16)
# plt.ylabel('房屋单价（元/平方米）', fontsize=16)
# plt.savefig("数据分析的那些图/房屋面积与房价的关系——散点图进阶")
# plt.show()


# 为了更明显地比较各行政区房屋面积对房价影响规律，对各区的散点进行最小二乘线性拟合：
# # 直线函数方程
# def linearfitting(x, A, B):
#     return A * x + B
#
#
# def plot_line():
#     plt.figure(figsize=(10, 8))
#     colors = ['red', 'red', 'red', 'red',
#               'blue', 'blue', 'blue', 'blue',
#               'green', 'green', 'green', 'green',
#               'gray', 'gray', 'gray', 'gray', 'gray']
#     district = ['昌平', '朝阳', '海淀', '丰台',
#                 '燕郊', '大兴', '通州', '西城',
#                 '顺义', '东城', '房山', '石景山',
#                 '亦庄开发区', '门头沟', '密云', '怀柔', '延庆']
#     markers = ['o', 's', 'v', 'x',
#                'o', 's', 'v', 'x',
#                'o', 's', 'v', 'x',
#                'o', 's', 'v', 'x', 'o']
#     for i in range(17):
#         x = data.loc[data['Dist'] == district[i]]["Area"]
#         y = data.loc[data["Dist"] == district[i]]['Price']
#         A, B = optimize.curve_fit(linearfitting, x, y)[0]
#         xx = np.arange(0, 2000, 100)
#         yy = A * xx + B
#         plt.plot(xx, yy, c=colors[i], marker=markers[i], label=district[i], linewidth=2)
#
#     plt.legend(loc=1, bbox_to_anchor=(1.138, 1.0), fontsize=12)
#
#     plt.title('北京各城区房屋面积对房价的影响（线性拟合）', fontsize=20)
#     plt.xlabel('房屋面积（平方米）', fontsize=16)
#     plt.ylabel('房屋单价（元/平方米）', fontsize=16)
#     plt.savefig('数据分析的那些图/房屋面积与房价的关系——散点图高阶')
#     plt.show()
#
#
# plot_line()

# 探究更容易受到人们青睐的二手房具有什么特点？
update_data = data.copy()  # 深度复制一份new_data数据,copy中的deep参数默认是True。

# 将分别加一后房源的关注人数和带看次数做乘积，用以表示房源的受欢迎程度，简记为受欢迎度
update_data['受欢迎度'] = (update_data['PeopleNumber'] + 1) * (update_data['WatchNumber'] + 1)
print(update_data.head())  # 查看updated_data的前五条数据
# 按找房源的受欢迎程度对所有房源进行降序排序，并提取出排名前500的房源信息
sort_by_popularity = update_data.sort_values(by='受欢迎度', ascending=False)
new_sort_by_popularity = sort_by_popularity[:500]
new_sort_by_popularity.head()  # 查看new_sort_by_popularity的前五条数据

# 区域分布数据
count_by_region_500_one = new_sort_by_popularity['Dist'].groupby(new_sort_by_popularity['Dist']).count()
count_by_region_500_two = count_by_region_500_one[count_by_region_500_one > 50]
count_by_region_500_two['其他区'] = count_by_region_500_one[count_by_region_500_one < 51].sum()
new_count_by_region_500 = count_by_region_500_two.sort_values(ascending=False)

# 户型分布数据
# 对不同户型的房子进行统计计数
count_by_house_type_500_one = new_sort_by_popularity['HouseType'].groupby(new_sort_by_popularity['HouseType']).count()
# 筛选出总数大于50套的户型
count_by_house_type_500_two = count_by_house_type_500_one[count_by_house_type_500_one > 60]
# 将总数小于50套的户型统一归为其他类
count_by_house_type_500_two['其他'] = count_by_house_type_500_one[count_by_house_type_500_one < 60].sum()
new_count_by_house_type_500 = count_by_house_type_500_two.sort_values(ascending=False)

# # 绘制饼形图
# fig, axes = plt.subplots(1, 2)
# new_count_by_region_500.plot(kind='pie', ax=axes[0], autopct='%.1f%%', startangle=90, label='')
# new_count_by_house_type_500.plot(kind='pie', ax=axes[1], autopct='%.1f%%', startangle=90, label='')
# # autopct参数的作用是指定饼形图中数据标签的显示方式
# # '%.1f%%'表示数据标签的格式是保留一位小数的百分数
# # startangle=90表示饼图的起始绘制角度是偏离x轴90度，并按逆时针绘制
# # label=''后，饼形图的左边便不会再显示Series对象的名字
#
# # 设置子图的标题以及设置饼形图的纵横比相等
# axes[0].set(title='区域分布', aspect='equal')
# axes[1].set(title='户型分布', aspect='equal')
# #
# plt.subplots_adjust(wspace=0.8)
# plt.suptitle('最受欢迎二手房特征分布饼形图')  # 设置figure对象的标题
# plt.savefig('数据分析的那些图/最受欢迎二手房特征分布饼形图')  # 保存图片


# # 绘制500套最受欢迎二手房面积频数分布直方图
# fig, axes = plt.subplots(figsize=(7, 5))
# new_sort_by_popularity['Area'].hist(ax=axes, bins=10)
# axes.set(xlabel='面积/平米', ylabel='数量/套', title='500套最受欢迎二手房面积频数分布直方图')
# plt.savefig('数据分析的那些图/500套最受欢迎二手房面积频数分布直方图')  # 保存图片
# plt.show()
