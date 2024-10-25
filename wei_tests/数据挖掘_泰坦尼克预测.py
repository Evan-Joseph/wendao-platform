import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import warnings

# 读取数据
df = pd.read_csv(r"D:\Personal\Desktop\train.csv", encoding='utf-8')

# 设置绘图风格
plt.style.use('fivethirtyeight')
sns.set()
warnings.filterwarnings('ignore')

# 生存率统计
df_survive = df['Survived'].value_counts(normalize=True)
n0_sample = df_survive[0]
n1_sample = df_survive[1]
print('死亡人数占{:.2%}; 幸存人数占{:.2%}'.format(n0_sample, n1_sample))

# 设置中文字体路径
myfont = matplotlib.font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")

# 绘制生存分布饼图
plt.figure()
df_counts = df['Survived'].value_counts()
plt.pie(df_counts, explode=(0, 0.1), labels=['未获救', '获救'],
        shadow=True, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('乘客生存分布', fontproperties=myfont, fontsize=15)
plt.legend(prop=myfont)
plt.show()

# 性别统计与生还率
print(df['Sex'].value_counts())
print()
print(df['Survived'].groupby(df['Sex']).value_counts())
print()
sur_fe = 233 / 314
sur_ma = 109 / 577
print("女性获救比例：{:.2%}；男性获救比例：{:.2%}".format(sur_fe, sur_ma))
print()

# 船舱等级与生还率
print(df['Pclass'].value_counts())
print()
print(df['Survived'].groupby(df['Pclass']).value_counts())
print()
sur_1 = 136 / 216
sur_2 = 87 / 184
sur_3 = 119 / 491
print("一号舱获救比例：{:.2%}；二号舱获救比例：{:.2%}；三号舱获救比例：{:.2%}".format(sur_1, sur_2, sur_3))

# 各船舱等级的生还率
sur_123 = [sur_1, sur_2, sur_3]

# 绘制不同船舱下乘客获救比例柱状图
plt.figure()
x = range(1, 4)
plt.bar(x, sur_123, color='g', label='不同船舱下的乘客获救比例')

plt.xlabel('船舱', fontproperties=myfont, fontsize=15)
plt.ylabel('获救比例', fontproperties=myfont, fontsize=15)
plt.title('不同船舱下乘客的获救率', fontproperties=myfont, fontsize=15)

# 设置 x 轴刻度标签
xtick_labels = ['{}号舱'.format(i) for i in x]
plt.xticks(x, xtick_labels, fontproperties=myfont)
plt.legend(prop=myfont)
plt.show()

# 各船舱及性别的生还率
sur_fe = [91/94, 70/76, 72/144]
sur_ma = [45/122, 17/108, 47/347]

# 绘制不同船舱及性别下的获救率折线图
plt.figure(figsize=(8,6), dpi=80, num=4)
x = range(1, 4)

plt.plot(x, sur_fe, color='r', label='女性获救比例', linewidth=2)
plt.plot(x, sur_ma, color='g', label='男性获救比例', linewidth=2)

plt.xlabel('船舱', fontproperties=myfont, fontsize=15)
plt.ylabel('获救比例', fontproperties=myfont, fontsize=15)
plt.title('不同船舱及不同性别下乘客的获救率', fontproperties=myfont, fontsize=15)

# 设置 x 轴刻度标签
xtick_labels = ['{}号舱'.format(i) for i in x]
plt.xticks(x, xtick_labels, fontproperties=myfont)
plt.legend(prop=myfont)
plt.show()
