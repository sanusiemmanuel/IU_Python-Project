import pandas as pd
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select, CustomJS, RangeSlider

# Visulise Train
def drawTrainGraph():
    train_df = pd.read_csv('train.csv') # import the dataset

    train = ColumnDataSource(data=train_df) #Convert dataset to bokeh dataset

    TOOLTIPS_TRAIN = [("Y1","@y1"), ("Y2","@y2"), ("Y3","@y3"), ("Y4","@y4")] #For the hover functionality of the graph

    # Train Dataset Figure
    train_fig = figure(x_axis_label="X", 
                y_axis_label="Y", 
                title = "Train",
                tooltips=TOOLTIPS_TRAIN)

    # Scatter graph for each coordinate
    y1_train_glyph = train_fig.circle(x="x", y="y1", color="green", source=train)
    y2_train_glyph = train_fig.circle(x="x", y="y2", color="red", source=train)
    y3_train_glyph = train_fig.circle(x="x", y="y3", color="purple", source=train)
    y4_train_glyph = train_fig.circle(x="x", y="y4", color="yellow", source=train)

    # Hide visibility
    y2_train_glyph.visible = False
    y3_train_glyph.visible = False
    y4_train_glyph.visible = False

    # Adding x and y range slider
    x_slider = RangeSlider(title="X", start=-25, end=25, value=(-25,25), step=1)
    x_slider.js_link("value", train_fig.x_range,"start", attr_selector=0)
    x_slider.js_link("value", train_fig.x_range,"end", attr_selector=1)

    y_slider = RangeSlider(title="Y", start=-50, end=8050, value=(-50,8050), step=1)
    y_slider.js_link("value", train_fig.y_range,"start", attr_selector=0)
    y_slider.js_link("value", train_fig.y_range,"end", attr_selector=1)

    #For Select Widget Functionality 
    menu_train = ["Y1","Y2", "Y3", "Y4"]

    jscode = """
        scatter_1.visible = false
        scatter_2.visible = false
        scatter_3.visible = false
        scatter_4.visible = false

        if (this.value == "Y4")  {				
            scatter_4.visible = true

        } else {		
            scatter_4.visible = false
        }

        if (this.value === "Y1") {
            scatter_1.visible = true		

        } else{
            scatter_1.visible = false
        } 
        
        if (this.value === "Y2")  {				
            scatter_2.visible = true
        } else {
            scatter_2.visible = false
        }
        
        if (this.value === "Y3")  {		
            scatter_3.visible = true

        } else {		
            scatter_3.visible = false
        }
    """

    callback = CustomJS(args=dict(
                        scatter_1=y1_train_glyph, 
                        scatter_2=y2_train_glyph,
                        scatter_3=y3_train_glyph,
                        scatter_4=y4_train_glyph),
                        code=jscode)

    train_menu = Select(options=menu_train, value="Y1", title="Y Coordinate")
    train_menu.js_on_change("value", callback)

    return column(train_menu, y_slider, train_fig, x_slider)