from wsgiref.simple_server import make_server
from hello_ import application

httpd = make_server('', 8000, application)

print('server is running at port 8000...')

httpd.serve_forever()