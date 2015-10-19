# coding=utf-8
# python 2.7
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import six
import rpcz
import search_pb2
import search_rpcz

class SearchService(search_rpcz.SearchService):
  def Search(self, request, reply):
    print("Got request for '%s'" % request.query)
    response = search_pb2.SearchResponse()
    response.results.append("result1 for " + request.query)
    response.results.append("this is result2")
    reply.send(response)

app = rpcz.Application()
server = rpcz.Server(app)
server.register_service(SearchService(), "SearchService")
server.bind("tcp://*:5555")
print("Serving requests on port 5555")
app.run()
