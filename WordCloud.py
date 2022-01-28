# https://www.cnblogs.com/wkfvawl/p/11585986.html    该文章提供了如何制作词云的相关知识
import imageio as imageio
import jieba  # 分词库
import pandas as pd
import wordcloud

df = pd.read_csv("bj副本.csv", encoding='gbk')
df['Quarters'].to_csv('词云/Quarters.txt', sep=" ", header=False, index=False)
df['Introduction'].to_csv('词云/Introduction.txt', sep=" ", header=False, index=False)


# Wordcloud-one
w1 = wordcloud.WordCloud(width=1000,
                         height=700,
                         background_color='white',
                         font_path='msyh.ttc',
                         scale=15)
f1 = open('词云/Quarters.txt', encoding='utf-8')
txt1 = f1.read()
w1.generate(txt1)
w1.to_file("词云/wordcloud-Quarters.jpg")


# wordcloud-two
mk = imageio.imread("词云/花生.jpg")
w2 = wordcloud.WordCloud(width=1000,
                         height=700,
                         background_color='white',
                         font_path='msyh.ttc',
                         mask=mk,
                         stopwords={"室", "厅", "万", "五年"},
                         scale=15)
f2 = open('词云/Introduction.txt', encoding='utf-8')
txt2 = f2.read()
txtlist = jieba.lcut(txt2)
string = " ".join(txtlist)
w2.generate(string)
w2.to_file("词云/wordcloud-Introduction.jpg")
