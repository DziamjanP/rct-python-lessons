import matplotlib.pyplot as plt
import numpy as np

import streamlit as st

import plots.func as func_plot

st.title("Plots of 4'th task")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Functions", "Bar chart", "Heatmap", "Pie chart", "Scatter", "3d"])

with tab1:
    tab1.write("Here are functions represented on the plot:")
    tab1.latex("g=\\begin{cases}e^{f(x)-b},&\\;0.5<xb<10\\\\\\sqrt{|f(x)+b|},&\\;0.1<xb<0.5\\\\2f(x)^2,&\\;\\textit{otherwise.}\\end{cases}")
    tab1.latex("b=\\begin{cases}ln(f(x))+(f(x)^2+y)^3,&\\;x/y>0\\\\ln|f(x)/y|+(f(x)+y)^3,&\\;x/y<0\\\\(f(x)^2+y)^3,&\\;x=0\\\\0,&\\;y=0.\\end{cases}")
    
    tab1.pyplot(func_plot.get_plot())