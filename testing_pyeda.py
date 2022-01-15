import pyeda
from pyeda.inter import *

f = expr("1 & (1 | 0)")

print(type(f))

g = f.to_dnf()

print(g)