# rpimodel
Get Raspberry Pi model Name(eg: A, B, B+...)

# install
pip install getrpimodel

# return
The 'Model' string of the [following Table.](http://elinux.org/RPi_HardwareHistory) 

Miner info in parentheses, like (Beta), (ECN0001), or (with BCM2837) are removed; or appear with '--s' option, or 'model_strict()' function

# How to use as python program
python -m getrpimodel [--s] 

# How to use as python library
import getrpimodel

print (getrpimodel.model())

print (getrpimodel.model_strict())

