import pandas as pd
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select, CustomJS, RangeSlider

# Visulise Assigned Dataset
def drawAssignedGraph():
    assigned_df = pd.read_csv('assigned_dataset.csv') # import the dataset

    assigned = ColumnDataSource(data=assigned_df) #Convert dataset to bokeh dataset

    TOOLTIPS_ASSIGNED = [("Y","@Y"), ("Delta Y","@Delta Y"), ("Y Deviation","@Y Deviation")] #For the hover functionality of the graph

    # Train Dataset Figure
    assigned_fig = figure(x_axis_label="X", 
                y_axis_label="Y", 
                title = "Assigned Dataset",
                tooltips=TOOLTIPS_ASSIGNED)

    # Scatter graph for each coordinate
    y1_assigned_glyph = assigned_fig.circle(x="X", y="Y", color="green", source=assigned)
    y2_assigned_glyph = assigned_fig.circle(x="X", y="Delta_Y", color="red", source=assigned)
    y3_assigned_glyph = assigned_fig.circle(x="X", y="Y_Deviation", color="purple", source=assigned)

    # Hide visibility
    y2_assigned_glyph.visible = False
    y3_assigned_glyph.visible = False

    # Adding x and y range slider
    x_slider = RangeSlider(title="X", start=-25, end=25, value=(-25,25), step=1)
    x_slider.js_link("value", assigned_fig.x_range,"start", attr_selector=0)
    x_slider.js_link("value", assigned_fig.x_range,"end", attr_selector=1)

    y_slider = RangeSlider(title="Y", start=-50, end=8050, value=(-50,8050), step=1)
    y_slider.js_link("value", assigned_fig.y_range,"start", attr_selector=0)
    y_slider.js_link("value", assigned_fig.y_range,"end", attr_selector=1)

    #For Select Widget Functionality 
    menu_assigned = ["Y", "Delta Y", "Y Deviation"]

    jscode_assigned = """
        scatter_1.visible = false
        scatter_2.visible = false
        scatter_3.visible = false

        if (this.value === "Y") {
            scatter_1.visible = true		

        } else{
            scatter_1.visible = false
        } 
        
        if (this.value === "Delta Y")  {				
            scatter_2.visible = true
        } else {
            scatter_2.visible = false
        }
        
        if (this.value === "Y Deviation")  {		
            scatter_3.visible = true

        } else {		
            scatter_3.visible = false
        }
    """

    callback = CustomJS(args=dict(
                        scatter_1=y1_assigned_glyph, 
                        scatter_2=y2_assigned_glyph,
                        scatter_3=y3_assigned_glyph),
                        code=jscode_assigned)

    assigned_menu = Select(options=menu_assigned, value="Y", title="Y Coordinate")
    assigned_menu.js_on_change("value", callback)

    return column( assigned_menu, y_slider, assigned_fig, x_slider )