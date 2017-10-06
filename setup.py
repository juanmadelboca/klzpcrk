"""setup module"""
from setuptools import setup

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(name='klzpcrk',
      version='0.1.0',
      description='Aplication to crack zip passwords',
      author='Del Boca Juan Manuel',
      author_email='juanmadelboca@gmail.com',
      packages=['dictionary',
                'klzipcrk'],
      install_requires=reqs,
      test_suite='nose.collector')