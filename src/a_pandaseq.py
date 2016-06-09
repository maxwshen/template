# Pairwise-align the paired end reads

import _config
import sys, os, fnmatch, datetime, subprocess
import numpy as np

from mylib import util


# Default params
DEFAULT_INP_DIR = _config.DATA_DIR + '2016-06-06/'
NAME = util.get_fn(__file__)


def combine_pairs(r1, r2, out_dir):
  out_fn = out_dir + _config.COMBINED_FN
  log_fn = out_dir + 'pandaseq_log.txt'
  subprocess.call('pandaseq -O ' + _config.MAXOVERLAP + ' -f ' + r1 + ' -r ' + r2 + ' -w ' + out_fn + ' -g ' + log_fn,
   shell = True)
  return


def main(inp_dir, out_dir, run = True):
  print NAME  
  util.ensure_dir_exists(out_dir)
  if not run:
    print '\tskipped'
    return out_dir

  reads1 = inp_dir + _config.READS_FN_1
  reads2 = inp_dir + _config.READS_FN_2
  print '\tCombining paired end reads:\n\t', \
    reads1, '\n\t', reads2
  combine_pairs(reads1, reads2, out_dir)

  return out_dir


if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1], sys.argv[2])
  else:
    main(DEFAULT_INP_DIR, _config.OUT_PLACE + NAME + '/')