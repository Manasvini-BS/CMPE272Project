import logging
import multiprocessing
import itertools

import numpy as np

from model_run import run_model, test_model
import model_run
import model_def
import settings
import util
import sys



if __name__ == '__main__':
 
  if(len(sys.argv) == 2 ):
    driverId = sys.argv[1]
    results = run_model((100, int(driverId), model_def.Model_GBC, model_run.get_data_accel_v2_svd, 1))
    predictions = list(results[0])
    testY = list(results[1])
    res=util.compute_auc(testY, predictions)
    print(res)

  
