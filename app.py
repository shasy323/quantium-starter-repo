import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load your processed data
df = pd.read_csv("formatted_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis"),  # Header

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)