#from distutils.core import setup
from setuptools import setup

with open("README.md") as f:
  long_description = f.read()

setup(
  name = 'getrpimodel',
  packages = ['getrpimodel'], # this must be the same as the name above
  version = '0.1.23',
  description = 'Get Raspberry Pi model Name(eg: A, B, B+...)',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Takeyuki UEDA',
  author_email = 'gde00107@nifty.com',
  license='MIT',
  url = 'https://github.com/UedaTakeyuki/getrpimodel', # use the URL to the github repo
  keywords = ['IoT', 'Raspberry Pi','model','revision'], # arbitrary keywords
  classifiers = ['Development Status :: 4 - Beta',
                 'Programming Language :: Python',
                 'Topic :: Terminals'
  ],
)
