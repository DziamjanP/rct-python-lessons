import matplotlib.pyplot as plt
import numpy as np

import streamlit as st

import plots.func as func_plot
import plots.bars as bar_plot
import plots.heatmap as heatmap

st.title("Plots of 4'th task")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Functions", "Bar chart", "Heatmap", "Pie chart", "Scatter", "3d"])

with tab1:
    st.write("Here are functions represented on the plot:")
    st.latex("g(x,b)=\\begin{cases}e^{f(x)-b},&\\;0.5<xb<10\\\\\\sqrt{|f(x)+b|},&\\;0.1<xb<0.5\\\\2f(x)^2,&\\;\\textit{otherwise.}\\end{cases}")
    b = st.number_input("b for g(x, b)", value=2)
    st.latex("b(x,y)=\\begin{cases}ln(f(x))+(f(x)^2+y)^3,&\\;x/y>0\\\\ln|f(x)/y|+(f(x)+y)^3,&\\;x/y<0\\\\(f(x)^2+y)^3,&\\;x=0\\\\0,&\\;y=0.\\end{cases}")
    y = st.number_input("y for b(x, y)", value=2)
    plot_range = st.slider("Select plot's range", -8.0, 8.0, (0.0, 2.0))
    st.pyplot(func_plot.get_plot(plot_range[0], plot_range[1], var_b=b, var_y=y))

with tab2:
    st.header("Horizontal bar chart")
    st.pyplot(bar_plot.get_plot())

with tab3:
    st.header("Random heatmap")
    size_x = st.slider("Horizontal size", 1, 20, 10)
    size_y = st.slider("Vertical size", 1, 20, 10)
    st.pyplot(heatmap.get_plot(size_x, size_y))
