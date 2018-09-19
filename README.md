# getrpimodel
Get Raspberry Pi model Name(eg: A, B, B+...)

## install

```bash:
pip install getrpimodel
```

## return
String: 'Model Name' same string as the 'Model' column value of the [following Table](http://elinux.org/RPi_HardwareHistory), like as "A", "B", "B+", "2 Model B", "3 Model B" and so on.

Miner info in parentheses, like (Beta), (ECN0001), or (with BCM2837) are removed; or appear with '--s' option, or 'model_strict()' function.

## How to use 
### as python program.

```bash:
python -m getrpimodel [--s] 
```

### as python library.

```python:
import getrpimodel

print (getrpimodel.model())
print (getrpimodel.model_strict())
```

### history
- 2018.09.19_version_0.1.13  add "Zero W", "3 Model B+"
