# 
from __future__ import division
import _config
import sys, os, fnmatch, datetime, subprocess
sys.path.append('/cluster/mshen/')
import numpy as np
from collections import defaultdict
from mylib import util
import pandas as pd
import matplotlib
matplotlib.use('Pdf')
import matplotlib.pyplot as plt
import seaborn as sns

# Default params
DEFAULT_INP_DIR = _config.OUT_PLACE + 'a_step/'
NAME = util.get_fn(__file__)

##
# Functions
##

##
# qsub
##
def gen_qsubs():
  # Generate qsub shell scripts and commands for easy parallelization
  print 'Generating qsub scripts...'
  qsubs_dir = _config.QSUBS_DIR + NAME + '/'
  util.ensure_dir_exists(qsubs_dir)
  qsub_commands = []

  num_scripts = 0
  for idx in range(0, 10):
    command = 'python %s.py %s' % (NAME, idx)
    script_id = NAME.split('_')[0]

    # Write shell scripts
    sh_fn = qsubs_dir + 'q_%s_%s.sh' % (script_id, idx)
    with open(sh_fn, 'w') as f:
      f.write('#!/bin/bash\n%s\n' % (command))
    num_scripts += 1

    # Write qsub commands
    qsub_commands.append('qsub -M maxwshen@csail.mit.edu -m e -wd %s %s' % (_config.SRC_DIR, sh_fn))

  # Save commands
  with open(qsubs_dir + '_commands.txt', 'w') as f:
    f.write('\n'.join(qsub_commands))

  print 'Wrote %s shell scripts to %s' % (num_scripts, qsubs_dir)
  return

##
# Main
##
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
