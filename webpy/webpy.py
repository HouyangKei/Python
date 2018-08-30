# -*- coding: utf-8 -*-

import json
import sys
from mysql import testLogin

import web
web.config.debug = False
urls = (
    '/index', 'index',
    '/login', 'login',
    '/blog.do', 'blog',
)
# 设置模板路径
sys.path.append('complete_path')
render = web.template.render('templates/')


app = web.application(urls, locals())

# 设置session
if web.config.get('_session') is None:
    session = web.session.Session(
        app, web.session.DiskStore('sessions'), {'username', ''})
    web.config._session = session
else:
    session = web.config._session

# 首页  查询列表


class index:
    name = ""

    def GET(self):
        # cookies  没有返回None
        #self.name = web.cookies().get("username")
        # session
        self.name = session.username
        print(session.username)
        # 那么为空没有登录过
        if self.name == '':
            print("没有登录过跳转到登录页面")
            return render.login()
        sql = testLogin.login()
        data = sql.selectPythonTest()
        sql.close()
        return render.index(self.name, data)


# 登录页
class login:

    def GET(self):
        return render.login()


# 登录方法
class blog:

    def POST(self):
        data = web.input()  # 获取参数值
        name = data.username  # 登录名
        pwd = data.password  # 登录密码
        # 查询数据库是否有用户名
        sql = testLogin.login()
        num = sql.login(name, pwd)
        sql.close()
        # 返回请求json串
        code = "1111"
        if int(num) > 0:
            # 保存登录信息
            # cookie
            # web.setcookie("username", name, 3000)
            # session
            session.username = name
            code = "0000"

        json_str = {
            'code': code,
            'username': name,
            'password': pwd
        }
        return json.dumps(json_str)


if __name__ == "__main__":
    app.run()
