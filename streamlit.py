#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:06:50 2022

@author: lomakomeiha
"""

import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go 

st.title("Loma's App")


data=pd.read_csv("/Users/lomakomeiha/Documents/GitHub/MSBA325/Data.csv")
data.rename(columns = {'Class':'Aptitude Level'}, inplace = True)

if st.checkbox('Show raw data'):
    st.subheader('raw data')
    st.write(data)
    

fig = px.scatter(data, x='AnnouncementsView', y='Discussion', size='raisedhands', color='gender',title='Student Participation by Gender')
st.plotly_chart(fig)


sub = data[['raisedhands', 'VisITedResources', 'AnnouncementsView', 'Discussion']]
corr=sub.corr(method='pearson')
fig2 = go.Figure(go.Heatmap(z=corr.values.tolist(),
                          x=sub.columns, y=sub.columns, colorscale='rdylgn'))
fig2.update_layout(title='Correlation Between Student Participation Variables')
st.plotly_chart(fig2)

fig3 = px.box(data, y='raisedhands', color='gender', title='Hands Raised by Gender')
st.plotly_chart(fig3)


option=st.selectbox("Grade level", ('All','Lower Level', 'Middle School', 'High School'))
if option=='All':
    fig4=px.histogram(data, x='VisITedResources', color='StageID', title='Visited Resources by Grade Level')
    st.plotly_chart(fig4)

if option=='Lower Level':
    lowerlevel=data[data["StageID"]=='lowerlevel']
    fig5=px.histogram(lowerlevel, x='VisITedResources', title='Visited Resources in Lower Level')
    st.plotly_chart(fig5)

if option=='Middle School':
    middleschool=data[data["StageID"]=='MiddleSchool']
    fig6=px.histogram(middleschool, x='VisITedResources', title='Visited Resources in Middle School', color_discrete_sequence=['red'])
    st.plotly_chart(fig6)
    st.info('Colors may vary from plot to plot')
    
if option=='High School':
    highschool=data[data["StageID"]=='HighSchool']
    fig7=px.histogram(highschool, x='VisITedResources', title='Visited Resources in High School', color_discrete_sequence=['green'])
    st.plotly_chart(fig7)
    st.info('Colors may vary from plot to plot')

dfg=data.groupby(['StudentAbsenceDays']).count()
fig5=px.bar(dfg, x=dfg.index,y=[191,289], title='Student Absence Days', 
           labels=dict(x="Student Absence Days", y="count"))
st.plotly_chart(fig5)


