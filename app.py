import streamlit as st
from PIL import Image
import glob
import json
import requests
import time

lst_resume = sorted([i.split('/')[-1] for i in  glob.glob("auto_label/image/*")])
st.title("Parser Resumes")
st.sidebar.title("Resume")

path_resume = st.sidebar.selectbox(label='Resume', options=lst_resume, index=1)
image = Image.open(f'auto_label/image/{path_resume}')

is_predict = st.button('Click here to predict')
if is_predict:
    start = time.time()
    predict_api = 'http://localhost:8010/api/predict'
    data = {'path': f'auto_label/image/{path_resume}'}
    response = requests.post(url=predict_api, data=json.dumps(data))
    total_time = time.time() - start
    image = response.content
    st.image(image, caption = 'Resume predict')
    st.text(f'Inference time: {total_time:0.4f} s')
else:
    st.image(image, caption = 'Resume original')