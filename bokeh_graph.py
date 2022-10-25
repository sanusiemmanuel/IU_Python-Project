from bokeh.io import show, output_file
from bokeh.layouts import layout, column, row, gridplot
import bokeh_test_graph
import bokeh_train_graph
import bokeh_choosen_graph
import bokeh_assigned_graph

def PlotGraph():
    train_layout = bokeh_train_graph.drawTrainGraph()
    test_layout = bokeh_test_graph.drawTestGraph()
    choosen_layout = bokeh_choosen_graph.drawChoosenGraph()
    assigned_layout = bokeh_assigned_graph.drawAssignedGraph()

    plots= [train_layout, test_layout, choosen_layout, assigned_layout]

    output_file(filename="Graph_Plotted.html")
    layout=gridplot(plots, ncols=2)
    show(layout)