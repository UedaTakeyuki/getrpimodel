from distutils.core import setup
setup(
  name = 'getrpimodel',
  packages = ['getrpimodel'], # this must be the same as the name above
  version = '0.1.8',
  description = 'Get Raspberry Pi model Name(eg: A, B, B+...)',
  author = 'Takeyuki UEDA',
  author_email = 'gde00107@nifty.com',
  license='MIT',
  url = 'https://github.com/UedaTakeyuki/getrpimodel', # use the URL to the github repo
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = ['Development Status :: 4 - Beta',
                 'Programming Language :: Python',
                 'Topic :: Terminals'
  ],
)
