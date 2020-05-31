import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

mobility_data = pd.read_csv('./../data/Global_Mobility_Report.csv')
mobility_aus = mobility_data.loc[mobility_data['country_region'] == 'Australia']
mobility_total = mobility_aus[:97]

data = pd.read_csv('./../data/owid-covid-data.csv')
data_aus = data[data['location'] == "Australia"]
# data_aus.to_csv('./../data/aus_covid_data.csv', index =False)

restrictions_borders_dates = ['2020-02-01', '2020-03-01', '2020-03-05', '2020-03-12',
                              '2020-03-16', '2020-03-19', '2020-03-24', '2020-03-28']
restrictions_mobility_dates = ['2020-03-13', '2020-03-18', '2020-03-23', '2020-03-30']
restrictions_borders_positions = [0,0,0,0,0,0,0,0]
restrictions_mobility_positions = [0,0,0,0]
restrictions_borders_text = ['China arrival blocked', 'Iran arrivals blocked',
                             'South Korean arrivals blocked', 'Italy arrivals blocked',
                             'Self-isolation for overseas travellers, cruise ships blocked for 30 days',
                             'Borders closed to non-citizens and residents',
                             'Ban on Australians travelling overseas',
                             'Mandatory isolation in hotels for all travellers']
restrictions_mobility_text = ['Outdoor gatherings limited to 500 persons',
                              'Indoor gatherings limited to 100 persons, outdoors still 500',
                              'Pubs / clubs closed, restaurants take-away only',
                              'Outdoor / indoor gatherings 2 persons only']

fig = make_subplots(rows=2, cols=3,
                    subplot_titles=("Retail and recreation", "Grocery and pharmacy", "Parks",
                                    "Transit stations", "Workplace", "Residental"),
                    shared_yaxes=True)

# Top left
fig.add_trace(
    go.Scatter(x=list(mobility_total.date),
               y=list(mobility_total.retail_and_recreation_percent_change_from_baseline),
               name="Retail and recreation", fill='tonexty', mode='none'), row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x=restrictions_borders_dates, y=restrictions_borders_positions, mode='markers',
               marker=dict(color=['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000']),
               name="Border restrictions ", text=restrictions_borders_text, textposition='top center'),
               row=1, col=1, secondary_y=False
               )

fig.add_trace(
    go.Scatter(x=restrictions_mobility_dates, y=restrictions_mobility_positions,
               mode='markers', marker=dict(color=['#fde725', '#fde725', '#fde725', '#fde725']),
               name="Mobility restrictions ", text=restrictions_mobility_text, textposition='top center'),
               row=1, col=1, secondary_y=False
               )


# Top mid
fig.add_trace(
    go.Scatter(x=list(mobility_total.date),
               y=list(mobility_total.grocery_and_pharmacy_percent_change_from_baseline),
               name="Grocery and pharmacy", fill='tonexty', mode='none'), row=1, col=2
)

fig.add_trace(
    go.Scatter(x=restrictions_borders_dates, y=restrictions_borders_positions, mode='markers',
               marker=dict(color=['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000']),
               name="Border restrictions ", text=restrictions_borders_text, textposition='top center'),
               row=1, col=2, secondary_y=False
               )

fig.add_trace(
    go.Scatter(x=restrictions_mobility_dates, y=restrictions_mobility_positions,
               mode='markers', marker=dict(color=['#fde725', '#fde725', '#fde725', '#fde725']),
               name="Mobility restrictions ", text=restrictions_mobility_text, textposition='top center'),
               row=1, col=2, secondary_y=False
               )


# Top right
fig.add_trace(
    go.Scatter(x=list(mobility_total.date),
               y=list(mobility_total.parks_percent_change_from_baseline),
               name="Parks", fill='tonexty', mode='none'), row=1, col=3
)

fig.add_trace(
    go.Scatter(x=restrictions_borders_dates, y=restrictions_borders_positions, mode='markers',
               marker=dict(color=['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000']),
               name="Border restrictions ", text=restrictions_borders_text, textposition='top center'),
               row=1, col=3, secondary_y=False
               )

fig.add_trace(
    go.Scatter(x=restrictions_mobility_dates, y=restrictions_mobility_positions,
               mode='markers', marker=dict(color=['#fde725', '#fde725', '#fde725', '#fde725']),
               name="Mobility restrictions ", text=restrictions_mobility_text, textposition='top center'),
               row=1, col=3, secondary_y=False
               )

# Bottom left
fig.add_trace(
    go.Scatter(x=list(mobility_total.date), y=list(mobility_total.transit_stations_percent_change_from_baseline),
               name="Transit stations", fill='tonexty', mode='none'), row=2, col=1
)

fig.add_trace(
    go.Scatter(x=restrictions_borders_dates, y=restrictions_borders_positions, mode='markers',
               marker=dict(color=['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000']),
               name="Border restrictions ", text=restrictions_borders_text, textposition='top center'),
               row=2, col=1, secondary_y=False
               )

fig.add_trace(
    go.Scatter(x=restrictions_mobility_dates, y=restrictions_mobility_positions,
               mode='markers', marker=dict(color=['#fde725', '#fde725', '#fde725', '#fde725']),
               name="Mobility restrictions ", text=restrictions_mobility_text, textposition='top center'),
               row=2, col=1, secondary_y=False
               )


# Bottom mid
fig.add_trace(
    go.Scatter(x=list(mobility_total.date),
               y=list(mobility_total.workplaces_percent_change_from_baseline),
               name="Workplace", fill='tonexty', mode='none'), row=2, col=2
)

fig.add_trace(
    go.Scatter(x=restrictions_borders_dates, y=restrictions_borders_positions, mode='markers',
               marker=dict(color=['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000']),
               name="Border restrictions ", text=restrictions_borders_text, textposition='top center'),
               row=2, col=2, secondary_y=False
               )

fig.add_trace(
    go.Scatter(x=restrictions_mobility_dates, y=restrictions_mobility_positions,
               mode='markers', marker=dict(color=['#fde725', '#fde725', '#fde725', '#fde725']),
               name="Mobility restrictions ", text=restrictions_mobility_text, textposition='top center'),
               row=2, col=2, secondary_y=False
               )


# Bottom right
fig.add_trace(
    go.Scatter(x=list(mobility_total.date), y=list(mobility_total.residential_percent_change_from_baseline),
               name="Residental", fill='tonexty', mode='none'), row=2, col=3
)

fig.add_trace(
    go.Scatter(x=restrictions_borders_dates, y=restrictions_borders_positions, mode='markers',
               marker=dict(color=['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000']),
               name="Border restrictions ", text=restrictions_borders_text, textposition='top center'),
               row=2, col=3, secondary_y=False
               )

fig.add_trace(
    go.Scatter(x=restrictions_mobility_dates, y=restrictions_mobility_positions,
               mode='markers', marker=dict(color=['#fde725', '#fde725', '#fde725', '#fde725']),
               name="Gathering restrictions ", text=restrictions_mobility_text, textposition='top center'),
               row=2, col=3, secondary_y=False
               )

# fig.update_layout(showlegend=False)

fig.update_layout(
    title_text="Google's community mobility reports for Australia with governmental restrictions <br>Change form baseline during covid-19 pandemic<br>"
)

# Set template
fig.update_layout(
    template="plotly_white"
)

fig.show()

directory = './../images/'
f = "mobility_plots.html"
file_path = os.path.join(directory, f)
fig.write_html(file_path)
os.chdir(directory)
print(os.path.abspath(f))