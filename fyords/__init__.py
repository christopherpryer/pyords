'''
TODO:
    -For comprehensive libraries such as this one, do I import each name-space
    here or would that not be efficient?
'''
from . import cluster
from . import base
from . import constraint_solver
from . import graph_solver
from . import learn
from . import linear_solver
from . import quant
from . import simulate
from . import util # maybe expose inner elements of util?
__version__ = '0.1.1'
