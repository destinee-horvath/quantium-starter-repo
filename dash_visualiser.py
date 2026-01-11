# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash()

# Define colours and text styles
colors = {
    'background': "#2B2A2C",
    'text': "#FFFFFF"
}

texts = { 
    'fontFamily': 'Helvetica, Arial, sans-serif',
}

#Load processed data 
df = pd.read_csv("processed_data/pink_morsels_sales.csv")

# Sort by date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create and format linechart 
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    labels={"date": "Date", "sales": "Sales", "region": "Region"}, 
    title="Pink Morsel sales by region (Jan 2021)", 
    template="plotly_dark"
)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    font_family=texts['fontFamily'],
    font=dict(size=10)
)

# Add vertical line for date of price increase 
fig.add_vline(
    x=pd.to_datetime("2021-01-15"),
    line_dash='dash', 
    line_color='yellow',
    line_width=3,
)

fig.update_layout(
    legend_title_text="Region (click to toggle)"
)

# Add annotation for price increase 
fig.add_annotation(
    x=pd.to_datetime("2021-01-15"),
    y=df["sales"].max()+100,
    text="Price increase (15 Jan 2021)",
    showarrow=True,
    arrowhead=2,
    ax=80,
    ay=-20,
    font=dict(color=colors["text"], size=12),
)

# When hovering, show vertical and horizontal line
fig.update_xaxes(
    rangeslider_visible=True, # Allows zooming in & navigating on x-axis
    showspikes=True,
    spikemode="across",
    spikesnap="cursor",
    showline=True,
    linewidth=0.5,
)

fig.update_yaxes(
    showspikes=True,
    spikemode="across",
    showline=True,
    linewidth=0.5
)


# Define layout of app 
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Pink Morsel Sales', 
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontFamily': texts['fontFamily'], 
            "marginBottom": "8px"
        }
    ),   

    html.Hr(),
    html.Br(),

    html.H3(children='Were sales higher before or after the Pink Morsel price increase on 15 Jan 2021?', style={
        'textAlign': 'center',
        'color': colors['text'], 
        'fontFamily': texts['fontFamily'], 
        "marginTop": "0px",  
    }),

    dcc.Graph(
        id='pink-morsel-sales-linechart', 
        figure=fig
    ), 
    
    html.Div(
        children=[
            html.P("Tips:", style={"fontWeight": "bold"}),
            html.P("- Use the slider below the chart to zoom the date range."),
            html.P("- Click legend items to show or hide regions."),
        ],
        style={
            "textAlign": "left",
            "color": colors["text"],
            "fontSize": "13px",
            "fontFamily": texts["fontFamily"],
            "marginLeft": "auto",
            "marginRight": "50px",
            "marginBottom": "50px",
            "border": "1px solid #555",
            "borderRadius": "6px",
            "padding": "10px 14px",
            "backgroundColor": "rgba(255, 255, 255, 0.03)",
            "maxWidth": "420px",
        }
    ),

    html.Br()
])


if __name__ == '__main__':
    app.run(debug=True)
