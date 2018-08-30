import matplotlib.pyplot as plt
import numpy as np

# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(8, 6), dpi=80)


# 柱子总数
N = 5
# 包含每个柱子对应值的序列
values = (25, 102, 66, 88, 110)
colors = ('red', 'black', '#7199cf', '#4fc4aa', '#e1a7a2')
x_titles = ('Jan', 'Fub', 'Mar', 'Apr', 'May')

# 包含每个柱子下标的序列
index = np.arange(N)

# 画柱形图


def columnarGraph():
    # 创建一个规格为 1 x 2 的子图 位置1
    plt.subplot(1, 2, 1)

    # 柱子的宽度
    width = 0.35
    # 设置横轴标签
    plt.xlabel('Months')
    # 设置纵轴标签
    plt.ylabel('money($)')
    # 添加标题
    plt.title('Monthly average rainfall')
    # 设置x轴每个柱子的标题
    plt.xticks(index, x_titles)

    # 添加纵横轴的刻度 总刻度为140，每个间距20
    plt.yticks(np.arange(0, 140, 20))

    # 添加图例
    plt.legend(loc="upper right")

    # 绘制柱状图
    p2 = plt.bar(index, values, width, label="rainfall")

    # 给每个柱子分配指定的颜色
    for bar, color in zip(p2, colors):
        bar.set_color(color)


def pieChart():
    # 创建一个规格为 1 x 2 的子图 位置2
    plt.subplot(1, 2, 2)
    # 添加标题
    plt.title('pieChart')

    # 生成标题、数值、百分比 列表      sum(values)： 元组求和  round(val,2)保留两位小数
    #['Jan\n25-money($)\n6.39%', 'Fub\n102-money($)\n26.09%']
    labels = ['{}\n{}-money($)\n{}%'.format(title, num, round(num / sum(values) * 100, 2))
              for title, num in zip(x_titles, values)
              ]

    print(labels)
    # 画饼状图，并指定标签和对应颜色
    plt.pie(values, labels=labels, colors=colors)


columnarGraph()
pieChart()
plt.show()
