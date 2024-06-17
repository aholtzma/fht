#!/usr/bin/env python

from distutils.core import Extension, setup
from numpy import get_include
from os.path import join
import os

# possible types
types = ("int", "long", "float", "double")

# generate sources
pth = os.getcwd()
template_file = join(os.getcwd(), "fht", "C_fht.template.c")
f = open(template_file, "r")
txt = f.read()
f.close()
for t in types:
    d = {"ctype":t}
    filled_txt = txt % d
    source = join(os.getcwd(), "fht", "C_fht_%(ctype)s.c" % d)
    f = open(source, "w")
    f.write(filled_txt)
    f.close()

# distutils

setup(name='fht',
      version='1.0.2',
      description='Fast Hadamard Transform',
      author='Nicolas Barbey',
      author_email='nicolas.a.barbey@gmail.com',
      packages=['fht'],
      ext_modules=[Extension('fht._C_fht_%(ctype)s' % {"ctype":t},
                             [join('fht', 'C_fht_%(ctype)s.c') % {"ctype":t}],
                             include_dirs=[join(get_include(), 'numpy')], )
                             #include_dirs=[get_include()], )
                   for t in types],
      )
