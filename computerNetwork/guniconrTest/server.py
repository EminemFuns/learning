import json
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:

def application(environ, start_response):
    start_response('401 OK', [('Content-Type', 'application/json')])
    return ['{"wang":"tianyi"}'.encode('utf-8'),]


httpd = make_server('', 8630, application)
print("Serving HTTP on port 8630...")
# 开始监听HTTP请求:
httpd.serve_forever()
