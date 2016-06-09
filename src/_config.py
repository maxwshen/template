

PRJ_DIR = '/cluster/mshen/prj/.../'  

toy = True
if toy:
  PRJ_DIR += 'toy/'
#######################################################
# Note: Directories should end in / always
#######################################################
DATA_DIR = PRJ_DIR + 'data/'
OUT_PLACE = PRJ_DIR + 'out/'
RESULTS_PLACE = PRJ_DIR + 'results/'
SRC_DIR = PRJ_DIR + 'src/'
#######################################################
#######################################################

CLEAN = False       # Values = 'ask', True, False

# toy = True
toy = False
if toy:
  pass
else:
  pass