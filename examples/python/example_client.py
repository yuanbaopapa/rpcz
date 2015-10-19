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

app = rpcz.Application()

stub = search_rpcz.SearchService_Stub(
    app.create_rpc_channel("tcp://127.0.0.1:5555"))

request = search_pb2.SearchRequest()
request.query = '元宝'
response = stub.Search(request, deadline_ms=1000)
print(response)
print(response.results)
