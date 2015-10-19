# coding=utf-8
# python 2.7
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import six

from rpcz import compiler
import os

my_bin_dir=os.path.abspath('../../../../../../bin/vc90/x86/debug')
os.environ['PATH']+=';'+my_bin_dir

compiler.generate_proto('../common/search.proto', '.')
compiler.generate_proto(
        '../common/search.proto', '.',
        with_plugin='python_rpcz', suffix='_rpcz.py',
        plugin_binary=
            my_bin_dir+r'\protoc-gen-python_rpcz.exe')
