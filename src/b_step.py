# 
from __future__ import division
import _config, _lib
import sys, os, fnmatch, datetime, subprocess
import numpy as np
from collections import defaultdict
from mylib import util
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Default params
DEFAULT_INP_DIR = _config.OUT_PLACE + 'a_step/'
NAME = util.get_fn(__file__)

# Functions



@util.time_dec
def main(inp_dir, out_dir):
  print NAME  
  util.ensure_dir_exists(out_dir)

  # Function calls

  return out_dir


if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(DEFAULT_INP_DIR, 
         _config.OUT_PLACE + NAME + '/', 
         sys.argv[1])
  else:
    main(DEFAULT_INP_DIR, _config.OUT_PLACE + NAME + '/')
