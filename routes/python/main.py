import logging
import multiprocessing
import itertools

import numpy as np

from model_run import run_model, test_model
import model_run
import model_def
import settings
import util

logging.root.setLevel(level=logging.INFO)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')

if __name__ == '__main__':
  print('starting main.py Manasvini')

  results = run_model((100, 3613, model_def.Model_GBC, model_run.get_data_accel_v2_svd, 1))

  pool = multiprocessing.Pool(processes=1)
  logging.info("Calling 1")
  #results = pool.map(
      #run_model,
      #map(lambda x: (100, x, model_def.Model_LR2, model_run.get_data_movements_accel, 1), settings.DRIVER_IDS[:1])
  #)

  print('Result got')
  print(results)
  print('For loop ------> ')
  for r in results:
  	print (r[1])
  print ('end')
  #predictions = np.array(list(itertools.chain(*[r[0] for r in results])))
  predictions = list(results[0])
  print('Predictoion : ')
  print(predictions)
  #testY = list(itertools.chain(*[r[-1] for r in results]))
  print('test Y')
  testY = list(results[1])
  print(testY)
  logging.info(util.compute_auc(testY, predictions))
