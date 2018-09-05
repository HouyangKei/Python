# -*- coding: utf-8 -*-
'''
Created on 2018年8月31日
抓取17k小说网的收藏榜数据
@author: hy
'''
import random
from urllib import request
from urllib.error import URLError, HTTPError

from bs4 import BeautifulSoup
from matplotlib import pyplot


class dbDemo:
    result = ""
    book_name = [] #书名
    book_nums = [] #榜单值
    user_names = []	#作者
    soup = ""
    top = 8 #前多少名
    colors = [] #颜色值
    # 请求地址
    url = "http://top.17k.com/top/top100/06_vipclick/06_vipclick_serialWithLong_top_100_pc.html"
    # 请求头
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}

    # 初始抓取页面类容
    def __init__(self):
        try:
            # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
            pyplot.figure(figsize=(11, 5), dpi=80)
            response = request.Request(self.url, headers=self.headers)
            html = request.urlopen(response)
            self.result = html.read().decode('utf-8')
            self.soup = BeautifulSoup(self.result)
            # print(self.result)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('错误原因是' + str(e.reason))
        except HTTPError as e:
            if hasattr(e, 'code'):
                print('错误状态码是' + str(e.code))

    # 获取当前前十名的书本名称
    def getBookName(self):
        # 解析 抓取到 名称部分  获取所有class为“red” 的a标签
        liResutl = self.soup.find_all('a', attrs={'class': 'red'})
        index = 0
        for ahtml in liResutl:
            # get_text文字内容
            if index < self.top:
                self.book_name.append(ahtml.text)
            index = index + 1
			
    # 获取当前前十名的榜单值和作者姓名
    def getBookNums(self):
        self.soup = BeautifulSoup(self.result)
        # 解析 获取class为 BOX的div元素
        liResutl = self.soup.find_all('div', attrs={'class': 'BOX'})
        # 拿取第一个  其他为分页
        table_res = liResutl[0]
        # print(table_res.prettify())
        # 拿去BOX下的 的td元素  nth-of-type(8)第8个td元素
        count_res = table_res.select("tr > td:nth-of-type(8)")
        # 拿去BOX下的 的td元素  nth-of-type(6)第6个td元素  下面的a标签
        users = table_res.select("tr > td:nth-of-type(6) > a")
        index = 0
        for count in count_res:
            if index < self.top:
                self.book_nums.append(count.text)
            else:
                index = 0
                break
            index = index + 1

        for user in users:
            if index < self.top:
                self.user_names.append(user.text)
            else:
                index = 0
                break
            index = index + 1

	#画饼图
    def pieChart(self):
        pyplot.rcParams['font.sans-serif'] = ['SimHei']
        pyplot.rcParams['axes.unicode_minus'] = False
        # 创建一个规格为 1 x 1 的子图 位置1
        pyplot.subplot(1, 1, 1)
        # 添加标题
        pyplot.title('17k小说网收藏榜单值排行')

        '''''ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', 
                shadow=True, startangle=90)'''
        # 相对于，去掉了阴影shadow=True
        labels = ['{}-{}'.format(title, num)
                  for title, num in zip(self.book_name, self.book_nums)
                  ]
        explode = (0, 0.1, 0, 0, 0, 0, 0, 0)
        pyplot.pie(self.book_nums,
                   explode=explode,
                   labels=labels,
                   colors=self.colors,
                   autopct='%1.1f%%',
                   shadow=False,
                   startangle=90,
                   # 设置文本标签的属性值,并且设置为白色
                   textprops={'fontsize': 12, 'color': 'white'},
                   )

        # Equal aspect ratio ensures that pie is drawn as a circle.
        pyplot.axis('equal')

        # 关键就是在于这里：添加一个图例
        pyplot.legend(loc='upper right')

        pyplot.show()
	
	#获取随机颜色值
    def randomcolor(self, num):
        colorArr = ['1', '2', '3', '4', '5', '6', '7',
                    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        colors = []
        for j in range(num):
            color = ""
            for i in range(6):
                color += colorArr[random.randint(0, 14)]
            colors.append("#" + color)
        return colors
db = dbDemo()
db.getBookName()
db.getBookNums()
db.colors = db.randomcolor(db.top)
print(db.book_name)
print(db.book_nums)
db.pieChart()
