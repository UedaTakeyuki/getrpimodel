# getrpimodel
Get Raspberry Pi model Name(eg: A, B, B+...)

## install

```bash:
pip install getrpimodel
```
## installs
[![Downloads](https://pepy.tech/badge/getrpimodel)](https://pepy.tech/project/getrpimodel)
[![Downloads](https://pepy.tech/badge/getrpimodel/month)](https://pepy.tech/project/getrpimodel)
[![Downloads](https://pepy.tech/badge/getrpimodel/week)](https://pepy.tech/project/getrpimodel)

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

## C++ version.
C++ version is also availabel as [here](https://github.com/UedaTakeyuki/GetRPimodel_cpp/blob/master/README.md).

## history
- 2018.09.19_version_0.1.13  add "Zero W", "3 Model B+"
- 2018.11.19_version_0.1.15  add "3 Model A+"
- 2020.05.01_version_0.1.16  merge [pr1](https://github.com/UedaTakeyuki/getrpimodel/pull/1) for adding model 4B by [shingon](https://github.com/shingon), thank you!
- 2020.05.01_version_0.1.16  add "Compute Module 3+"
- 2020.05.01_version_0.1.16  add missing b+ of rev "900032"
- 2020.09.05_version_0.1.17  fix [issue#2](https://github.com/UedaTakeyuki/getrpimodel/issues/2). Thanks [goszpeti](https://github.com/goszpeti)!
- 2020.09.08_version_0.1.19  merge [issue#3](https://github.com/UedaTakeyuki/getrpimodel/issues/3). Thanks [Fabian Affolter](https://github.com/fabaff)!
- 2021.03.25_version_0.1.20  add rev 1.4 PCB's of RPi4
- 2022.02.16_version_0.1.21  merge [issue#4](https://github.com/UedaTakeyuki/getrpimodel/issues/4). Thanks [SimonLamy](https://github.com/SimonLamy)!
- 2023.02.14_version_0.1.22  merge [issue#5](https://github.com/UedaTakeyuki/getrpimodel/issues/5). Thanks [Sergei Guselnikov](https://github.com/arietis)!
- 2023.02.14_version_0.1.23  add rev 1.5 PCB's of RPi4