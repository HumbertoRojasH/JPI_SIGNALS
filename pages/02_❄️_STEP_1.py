import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from data import *
st.set_page_config(layout="wide")
@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


st.markdown("# INPUT DATA")
st.sidebar.markdown("# INPUT DATA")

file = st.file_uploader("Upload a file")

if  file is not None:
    Data.file = file
    Data.acc = np.genfromtxt(Data.file)

if Data.file is not None:

    hz = st.sidebar.text_input("SAMPLING FREQUENCY (Hz)", value=200)
    Data.dt = 1/float(hz)

    n = st.sidebar.text_input("NUMBER OF SAMPLES", value=str(len(Data.acc)))
    Data.n = int(n)

    fac = st.sidebar.text_input("FACTOR CONVERTION TO (cm/s2)", value=1)
    Data.fac = float(fac)

    Data.df = pd.DataFrame()
    Data.df["Time"] = np.arange(0, Data.n*Data.dt, Data.dt)
    Data.df["Acc"] = Data.acc[0:Data.n]*Data.fac
    Data.Int_vel(Data)

    st.write("## Uncorrected data:")

    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05)
    fig.add_scatter(x=Data.df["Time"],y=Data.df["Acc"],line=dict(color='blue',width=1), row=1, col=1)
    fig.add_scatter(x=Data.df["Time"],y=Data.df["Vel"],line=dict(color='blue',width=1), row=2, col=1)
    fig.add_scatter(x=Data.df["Time"],y=Data.df["Dis"],line=dict(color='blue',width=1), row=3, col=1)
    
    fig.update_yaxes(title_text="Acceleration (cm/s2)", row=1, col=1)
    fig.update_yaxes(title_text="Velocity (cm/s)",row=2, col=1)
    fig.update_yaxes(title_text="Displacement (cm)", row=3, col=1)

    fig.update_xaxes(title_text="Time (s)", row=3, col=1)

    fig.update_layout(
        height=900,autosize=False,
        showlegend=False)
    st.plotly_chart(fig,use_container_width=True)
    
    st.write(Data.df)

    csv = convert_df(Data.df)
    dw = st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='uncorrected_data.csv',
    mime='text/csv')



