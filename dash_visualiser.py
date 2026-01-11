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
    )
])


if __name__ == '__main__':
    app.run(debug=True)
