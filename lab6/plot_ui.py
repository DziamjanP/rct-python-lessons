import matplotlib.pyplot as plt
import numpy as np

import streamlit as st

import plots.func as func_plot
import plots.bars as bar_plot
import plots.heatmap as heatmap
import plots.pie as pie_chart
import plots.scatter as scatter_plot
import plots.plot_3d as plot_3d

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

with tab4:
    st.header("Pie chart of fruit favors of some users")
    st.pyplot(pie_chart.get_plot())

with tab5:
    st.header("Scatter plot of 3 random clusters")
    st.text("Cluster sizes and positions can be adjusted with sliders.")
    cluster_size = st.slider("Cluster size", 1, 500, 50)
    cluster_sigm = st.slider("Sigma value of cluster", 0.0, 5.0, 0.4)
    st.text("Position of red cluster:")
    ax = st.number_input("Red cluster x", value=1)
    ay = st.number_input("Red cluster y", value=1)
    st.text("Position of green cluster:")
    bx = st.number_input("Green cluster x", value=5)
    by = st.number_input("Green cluster y", value=2)
    st.text("Position of blue cluster:")
    cx = st.number_input("Blue cluster x", value=3)
    cy = st.number_input("Blue cluster y", value=4)
    st.pyplot(scatter_plot.get_plot(positiona=(ax, ay), positionb=(bx, by), positionc=(cx, cy), cluster_size=cluster_size, cluster_sigma=cluster_sigm))

with tab6:
    st.header("3-dimensional plot of function:")
    st.latex("z=sin(\\sqrt{x^2+y^2})")
    x_range = st.slider("Select plot's X range", -10.0, 10.0, (-5.0, 5.0))
    y_range = st.slider("Select plot's Y range", -10.0, 10.0, (-5.0, 5.0))
    st.pyplot(plot_3d.get_plot(x_range[0], x_range[1], y_range[0], y_range[1]))