import pdb
from wsgiref import simple_server
from tutorial import create_app

if __name__ == '__main__':
  application = create_app()
  httpd = simple_server.make_server('127.0.0.1', 8000, application)
  pdb.run('httpd.serve_forever()')
