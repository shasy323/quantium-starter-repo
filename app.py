import pandas
from dash import Dash, html, dcc, Input, Output

from plotly.express import line

# the path to the formatted data file
DATA_PATH = "./formatted_data.csv"
COLORS = {
    "primary": "#F5F7FA",   # light grey background
    "secondary": "#FFFFFF", # white cards
    "accent": "#4A90E2",    # soft blue
    "font": "#2C3E50"       # dark grey text
}

# load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="Date")

# initialize dash
dash_app = Dash(__name__)


# create the visualization
def generate_figure(chart_data):
    line_chart = line(chart_data, x="Date", y="Sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )

    line_chart.update_traces(line=dict(color=COLORS["accent"]))
    return line_chart


visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "backgroundColor": COLORS["secondary"],
        "color": COLORS["font"],
        "padding": "15px",
        "borderRadius": "10px",
        "boxShadow": "0px 2px 8px rgba(0,0,0,0.1)"
    }
)

# region picker
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [region_picker],
    id="region_picker",
    style={
        "fontSize": "120%",
        "marginTop": "20px"
    }
)


# define the region picker callback
@dash_app.callback(
    Output("visualization", "figure"),
    Input("region_picker", "value")
)
def update_graph(region):
    # filter the dataset
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["Region"].str.lower() == region]

    # generate a new line chart with the filtered data
    figure = generate_figure(trimmed_data)
    return figure


# define the app layout
dash_app.layout = html.Div(
    [
        header,
        visualization,
        region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "backgroundColor": COLORS["primary"],
        "padding": "30px"
    }
)

# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run(debug=True)