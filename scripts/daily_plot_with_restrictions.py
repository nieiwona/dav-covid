import pandas as pd
import plotly.graph_objects as go
import os
import sys

data = pd.read_csv('./../data/owid-covid-data.csv')
data_aus = data[data['location'] == "Australia"]
# data_aus.to_csv('./../data/aus_covid_data.csv', index =False)

restrictions_dates = ['2020-03-01', '2020-04-01']
restrictions_data_aus = data_aus.loc[data_aus['date'].isin(restrictions_dates)]
restrictions_data_aus_list = restrictions_data_aus['new_cases'].tolist()
restrictions_positions = [x+50 for x in restrictions_data_aus_list]
restrictions_text = ['Iran + China arrivals blocked', 'lalal']

# print(len(restrictions_dates))
# print(len(restrictions_positions))
# print(len(restrictions_text))


# Create figure
fig = go.Figure()

fig.add_trace(
    go.Bar(x=list(data_aus.date), y=list(data_aus.new_cases),
           name="New cases"))


fig.add_trace(
    go.Scatter(x=restrictions_dates, y=restrictions_positions, mode='markers+text',
               name="Restrictions", text=restrictions_text, textposition='top center'))




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

# directory = './../images/'
# f = "daily_plot_with_restrictions.html"
# file_path = os.path.join(directory, f)
# fig.write_html(file_path)
# os.chdir(directory)
# print(os.path.abspath(f))
