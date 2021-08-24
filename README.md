# pyMaxPro\_lite

Simple MaxPro space-filling algorithm implementation in python.

The code utilizes MaxPro criterion described in [V. Roshan Joseph, Evren Gul, and Shan Ba (2015)](https://doi.org/10.1093/biomet/asv002), but does not contain fancy functionalities that the original authors implemented in R language.

## How to install

### You may create or use anaconda environment to control over the packages used in your project.

Create environment:
```
conda create -y --name custom-env-name python=3.8
conda activate custom-env-name
```

or activate existing environment:
```
conda activate custom-env-name
```

### Install prerequisite packages.

Install following packages from conda-forge channel:
* SciPy
* NumPy

```
conda install -c conda-forge scipy numpy
```

### Clone and install pyMaxPro\_lite.

Clone from github to local storage, and checkout branch if necessary:
```
git clone https://github.com/yonghoonlee/pyMaxPro_lite.git
cd pyMaxPro_lite
git checkout branch-name
```

Install pyMaxPro\_lite:
```
python setup.py develop
```

## How to use

Run following simple code:
```
from pymaxpro_lite.maxpro import maxpro_design
d = maxpro_design()
d.n = 8
d.p = 3
x = d.solve()
print(x)
```

then you will get:
```
[[9.18972072e-01 7.31505609e-01 5.91135883e-01]
 [3.60570411e-05 4.26330655e-01 7.78425090e-01]
 [7.42082749e-01 5.24189855e-01 4.38276579e-04]
 [2.25781710e-01 9.99759184e-01 2.80936313e-01]
 [9.99995556e-01 3.41777594e-04 9.99445511e-01]
 [9.25104488e-02 4.34303173e-02 8.66445617e-02]
 [5.62380386e-01 2.01882624e-01 4.36223971e-01]
 [4.53881879e-01 8.68993411e-01 9.36525545e-01]]
```

## Reference

Joseph, V.R., Gul, E., Ba, S., (2015) "Maximum projection designs for computer experiments," *Biometrika*, **102**(*2*):371–380.
