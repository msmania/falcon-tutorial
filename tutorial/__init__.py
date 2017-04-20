import falcon
from tutorial.api.resources import Resource

def create_app():
  api = falcon.API()
  images = Resource()
  api.add_route('/images', images)
  return api
