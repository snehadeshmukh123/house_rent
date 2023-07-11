import pickle
import json
import numpy as np
import config
model_file_name= config.MODEL_FILE_PATH


class HouseRent():
   def __init__(self,area):
      self.area = area
      

   def __load_saved_data(self):
       with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

   def get_predicted_price(self):
       self.__load_saved_data()

       test_array = np.zeros([1,self.model.n_features_in_])
       test_array[0,0] = self.area

       predicted_charges = np.around(self.model.predict(test_array)[0],3)
       return predicted_charges