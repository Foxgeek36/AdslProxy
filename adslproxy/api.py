# coding=utf-8
import json
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler, Application
from adslproxy.config import *

'''
[api接口模块]
'''


class MainHandler(RequestHandler):
    def initialize(self, redis):
        self.redis = redis
    
    def get(self, api=''):
        # 首页初始提醒
        if not api:
            links = ['random', 'proxies', 'names', 'all', 'count']
            # write->该方法将获取到的字符串内容显示在端口打开页面中
            self.write('<h4>Welcome to ADSL Proxy API</h4>')
            for link in links:
                self.write('<a href=' + link + '>' + link + '</a><br>')

        # 获取随机代理
        if api == 'random':
            result = self.redis.random()
            if result:
                self.write(result)

        # 获取主机列表/ 唯一标志
        if api == 'names':
            result = self.redis.names()
            if result:
                self.write(json.dumps(result))

        # 获取代理列表
        if api == 'proxies':
            result = self.redis.proxies()
            if result:
                self.write(json.dumps(result))

        # 获取所有映射关系
        if api == 'all':
            result = self.redis.all()
            if result:
                self.write(json.dumps(result))

        # 获取代理数量
        if api == 'count':
            self.write(str(self.redis.count()))


def server(redis, port=API_PORT, address=''):
    # attention +++
    application = Application([
        (r'/', MainHandler, dict(redis=redis)),
        (r'/(.*)', MainHandler, dict(redis=redis)),
    ])
    # tornado监听对应的端口
    application.listen(port, address=address)
    print('ADSL API Listening on', port)
    # web服务开启 +--
    tornado.ioloop.IOLoop.instance().start()
