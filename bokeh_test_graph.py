import pandas as pd
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeSlider, Select

def drawTestGraph():
        
    # V0isualization For Test Dataset
    test_df = pd.read_csv('test.csv')

    test = ColumnDataSource(data=test_df)

    TOOLTIPS_TEST = [("Y","@y")]
    #Visualize Train Dataset
    test_fig = figure(x_axis_label="X", 
                y_axis_label="Y",
                title = "Test", 
                tooltips=TOOLTIPS_TEST)                

    y_test_glyph = test_fig.circle(x="x", y="y", color="green", source=test)

    # Adding x and y range slider
    x_slider = RangeSlider(title="X", start=-25, end=25, value=(-25,25), step=1)
    x_slider.js_link("value", test_fig.x_range,"start", attr_selector=0)
    x_slider.js_link("value", test_fig.x_range,"end", attr_selector=1)

    y_slider = RangeSlider(title="Y", start=-50, end=8050, value=(-50,8050), step=1)
    y_slider.js_link("value", test_fig.y_range,"start", attr_selector=0)
    y_slider.js_link("value", test_fig.y_range,"end", attr_selector=1)

    
    #For Select Widget Functionality 
    menu_train = ["Y"]
    test_menu = Select(options=menu_train, value="Y", title="Y Coordinate")
    return column(test_menu, y_slider, test_fig, x_slider)