import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Display Image')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
    )

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'あなたのコンディション：', condition

# #
# df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
# #     columns=['lat', 'lon']
# )
# df
# st.table(df.style.highlight_max(axis=0))
# st.map(df)


# cd C:\Users\Mami\Documents\Python
# streamlit run c:\Users\Mami\Documents\Python\Streamlit_training.py