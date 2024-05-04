Traceback (most recent call last):
  File "kan.py", line 7, in <module>
    from kan import *
  File "C:\Users\TologonovAB\Desktop\Модель для общей линии\kan.py", line 45, in <module>
    model = KAN(width=[2,5,1], grid=5, k=3, seed=0)
NameError: name 'KAN' is not defined


__init__.py
import torch
from .KAN import *

torch.set_default_dtype(torch.float64)

KAN.py
import torch
import torch.nn as nn
import numpy as np
from .KANLayer import *
from .Symbolic_KANLayer import *
from .LBFGS import *
import os
import glob
import matplotlib.pyplot as plt
from tqdm import tqdm
import random
import copy


class KAN(nn.Module):
    '''
    KAN class
    
    Attributes:
