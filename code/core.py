# Convenience functions
def ind_max(x):
  m = max(x)
  return x.index(m)

# Need access to random numbers
import random
import numpy as np
import matplotlib.pyplot as plt
# Definitions of bandit arms
from arms.adversarial import *
from arms.bernoulli import *
from arms.normal import *
from arms.rewards import * 
# Definitions of bandit algorithms

from algorithms.exp3.exp3 import *
from algorithms.exp3ix.exp3ix import *

# # Testing framework
from testing_framework.tests import *
