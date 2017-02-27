import sys
import __init__ as getrpimodel

usage = 'Usage: python {} [--s]'.format(__file__)

if len(sys.argv) == 1:
  print (getrpimodel.model())
elif len(sys.argv) == 2:
  if sys.argv[1] == '--s':
    print (getrpimodel.model_strict())
  else:
    print usage
else:
  print usage
