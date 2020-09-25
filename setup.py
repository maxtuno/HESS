import sys
import setuptools
from distutils.core import setup, Extension
ext_modules = [
    Extension("libhess",
              language="c",
              sources=['src/libhess.c'],
              include_dirs=['include'],
              ),
]
setup(
    name='HESS',
    version='0.0.1',
    packages=['hess'],
    url='http://www.peqnp.com',
    license='Copyright (c) 2012-2020 Oscar Riveros. All rights reserved.',
    author='Oscar Riveros',
    author_email='contact@peqnp.science',
    description='HESS black-box algorithm from http://www.peqnp.com',
    ext_modules=ext_modules,
)
