import streamlit as st
#from zipfile import ZipFile
#from pathlib import Path
#import glob
#import timeit
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

st.set_page_config('COSCO MNR', page_icon="🏟️", layout='wide')

def title_main(url):
     st.markdown(f'<h1 style="color:#230c6e;font-size:42px;border-radius:2%;"><br>{url}</h1>', unsafe_allow_html=True)

def success_df(html_str):
    html_str = f"""
        <p style='background-color:#baffc9;
        color: #313131;
        font-size: 15px;
        border-radius:5px;
        padding-left: 12px;
        padding-top: 10px;
        padding-bottom: 12px;
        line-height: 18px;
        border-color: #03396c;
        text-align: left;'>
        {html_str}</style>
        <br></p>"""
    st.markdown(html_str, unsafe_allow_html=True)

title_main('COSCO MNR Containers Photos Upload 🚛 🚢')
st.divider()
if st.button('Success'):
    success_df('Success!')
if __name__ == '__main__':
    app.run(debug=True)
