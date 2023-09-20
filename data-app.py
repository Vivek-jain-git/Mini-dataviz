import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')
df=pd.read_csv('india.csv')
l=sorted(df['State name'].unique())
l.insert(0,'All India')
l1=sorted(df.columns[5:])
st.sidebar.title('India Data Visualization')
sstate=st.sidebar.selectbox('Select a State',l)
prim=st.sidebar.selectbox('Select Primary parameter',l1)
sec=st.sidebar.selectbox('Select Secondary parameter',l1)
plot=st.sidebar.button('Plot Graph')
if plot:
    st.text("Size --> Primary Parameter")
    st.text("Color --> Secondary Parameter")
    if sstate=='All India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=4, mapbox_style='carto-positron',size=prim,color=sec,width=1000,height=800,hover_name='District name')
        st.plotly_chart(fig,use_container_width=True)
    else:
        fig = px.scatter_mapbox(df[df['State name']==sstate], lat="Latitude", lon="Longitude", zoom=5, mapbox_style='carto-positron', size=prim,color=sec, width=1200, height=800,hover_name='District name')
        st.plotly_chart(fig,use_container_width=True)