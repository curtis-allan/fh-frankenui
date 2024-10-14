"""Data Structures and Utilties"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../lib_nbs/00_foundation.ipynb.

# %% auto 0
__all__ = ['stringify', 'str2ukcls', 'VEnum']

# %% ../lib_nbs/00_foundation.ipynb
from enum import Enum, auto
from fastcore.all import *

# %% ../lib_nbs/00_foundation.ipynb
# need a better name, stringify might be too general for what it does 
def stringify(o # String, Tuple, or Enum options we want stringified
             ): # String that can be passed FT comp args (such as `cls=`)
    "Converts input types into strings that can be passed to FT components"  
    if is_listy(o): return ' '.join(map(str,o)) if o else ""
    return o.__str__()

# %% ../lib_nbs/00_foundation.ipynb
def str2ukcls(base, txt): return f"uk-{base}-{txt.replace('_', '-')}".strip('-')

# %% ../lib_nbs/00_foundation.ipynb
class VEnum(Enum):
    def __str__(self): return self.value
    def __add__(self, other): return stringify((self,other))
    def __radd__(self, other): return stringify((other,self))
