import numpy as np 
import pickle

loaded_model= pickle.load(open('/content/DetectionSystem.py', 'rb'))

input_data = (146,0,0,0,0,13,1,0.0,0.0)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The network is not intruded')
elif (prediction[0] == 1):
  print('The network is intruded by DoS')
elif (prediction[0] == 2):
  print('The network is intruded by Probe')
elif (prediction[0] == 1):
  print('The network is intruded by R2L')
else :
  print('The network is intruded by U2R')