# main2.py

from sys import path

path.append('..\\packages')

import extra.iota

print(extra.iota.FunI())

# main2.py

from extra.iota import FunI

print(FunI())