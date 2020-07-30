import streamlit as st
import numpy as np
import pandas as pd
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests

url = 'http://127.0.0.1:8000'


def _formatter(res):
    result = res[3:-2].split(',')
    return result


st.write("""
# Recommendation App
""")

st.subheader('NCF Recommendation')
st.write('Put the user ID and get the top three recommended snacks')
user_input_ncf = st.text_input('User ID for NCF')
if user_input_ncf:
    query = url + '/ncf/' + user_input_ncf
    r = requests.get(query)
    if r.status_code == 200:
        result = _formatter(str(r.content))
        for res in result:
            st.write(res.split(':')[1])
    else:
        st.write('No recommendation based on input information')

st.subheader('NPA Recommendation')
st.write('Put the user ID and get the top three recommended properties the user like')
user_input_npa = st.text_input('User ID for NPA')
if user_input_npa:
    query = url + '/npa/' + user_input_npa
    r = requests.get(query)
    if r.status_code == 200:
        result = _formatter(str(r.content))
        for res in result:
            st.write(res)
    else:
        st.write('No recommendation based on input information')
