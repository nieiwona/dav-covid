import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio


data = pd.read_csv('./../data/owid-covid-data.csv')
data_aus = data[data['location'] == "Australia"]
# data_aus.to_csv('./../data/aus_covid_data.csv', index =False)


# Create figure
fig = go.Figure()

fig.add_trace(
    go.Bar(x=list(data_aus.date), y=list(data_aus.new_cases)))

# Set title
fig.update_layout(
    title_text="New cases of covid-19 in Australia daily"
)

# Set template
fig.update_layout(
    template="plotly_white"
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=7,
                     label="1w",
                     step="day",
                     stepmode="backward"),
                dict(count=14,
                     label="2w",
                     step="day",
                     stepmode="backward"),
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=2,
                     label="2m",
                     step="month",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()