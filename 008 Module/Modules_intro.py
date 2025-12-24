# Module : a file containing code you want to include in your programe
# use "import" to include a module (built-in or your own)
# useful to break up a large program reusable seperate files

import math
print(math.pi)

# using alices
import math as m
print(m.pi)

# import specific part from a module
from math import pi
print(pi)

import example as e
print(e.my_pi)
print(e.squreNum(10))
print(e.cubeNum(10))
