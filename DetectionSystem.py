
import numpy as np
import pickle
import streamlit as st

loaded_model= pickle.load(open('E:/project2/trained_model9.sav', 'rb'))

#creating a function
def netPred(input_data):
  input_data_as_numpy_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
  prediction = loaded_model.predict(input_data_reshaped)
  print(prediction)
  if (prediction[0] == 0):
    return 'The network is not intruded'
  elif (prediction[0] == 1):
    return 'The network is intruded by DoS'
  elif (prediction[0] == 2):
    return 'The network is intruded by Probe'
  elif (prediction[0] == 1):
    return 'The network is intruded by R2L'
  else :
    return 'The network is intruded by U2R'

def main():
  st.title('Network Intrusion Detection System Web App')
  
  src=st.text_input('input for src_bytes')
  dst=st.text_input('input for dst_bytes')
  li=st.text_input('input for logged_in')
  nc=st.text_input('input for num_comprimised')
  rs=st.text_input('input for root_shell')
  count=st.text_input('input for count')
  sc=st.text_input('input for srv_count')
  sr=st.text_input('input for serror_rate')
  ssr=st.text_input('input for srv_serror_rate')

  res = ""

  if(st.button('Predict')):
    res = netPred([src,dst,li,nc,rs,count,sc,sr,ssr])
  
  st.success(res)


if __name__ == '__main__':
  main()
