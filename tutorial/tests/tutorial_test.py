import pytest

def test_resource(client):
  resp = client.simulate_get('/images')
  assert(resp.status_code == 200)
  assert(resp.json == {u'message': u'Hello world!'})

  resp = client.simulate_get('/invalid')
  assert(resp.status_code == 404)
