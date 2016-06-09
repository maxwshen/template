# affine gap alignment of combined reads
# against expected genome

import _config
import sys, os, fnmatch, datetime, subprocess
import numpy as np
from Bio import SeqIO
from Bio.Seq import Seq

from mylib import util


# Default params
DEFAULT_INP_DIR = _config.OUT_PLACE + 'a_pandaseq/'
NAME = util.get_fn(__file__)


def seq_align(inp_fn, out_fn):
  util.exists_empty_fn(out_fn)

  sa_tool = '/cluster/mshen/tools/seq-align/bin/needleman_wunsch'
  sa_options = '--freestartgap --freeendgap --match 10 --mismatch -8 --gapopen -20 --gapextend -1'

  timer = util.Timer()
  rs = SeqIO.parse(inp_fn, 'fasta')
  outf = open(out_fn, 'a')
  while True:
    try:
      r = rs.next()
      ans = subprocess.check_output(' '.join([sa_tool, 
        sa_options, 
        str(r.seq), 
        _config.GENOME]),
        shell = True)

      outf.write('>' + r.id + '\n' + ans.rstrip() + '\n')
      timer.update(print_progress = True)

    except StopIteration:
      print '\tcomplete'
      break

  
  return


def main(inp_dir, out_dir, run = True):
  print NAME  
  util.ensure_dir_exists(out_dir)
  if not run:
    print '\tskipped'
    return out_dir

  inp_fn = inp_dir + _config.COMBINED_FN
  out_fn = out_dir + _config.COMBINED_FN
  seq_align(inp_fn, out_fn)

  return out_dir


if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1], sys.argv[2])
  else:
    main(DEFAULT_INP_DIR, _config.OUT_PLACE + NAME + '/')
