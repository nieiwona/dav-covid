import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

mobility_data = pd.read_csv('./../data/Global_Mobility_Report.csv')
mobility_aus = mobility_data.loc[mobility_data['country_region'] == 'Australia']
mobility_total = mobility_aus[:97]

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

# Top mid
fig.add_trace(
    go.Scatter(x=list(mobility_total.date),
               y=list(mobility_total.grocery_and_pharmacy_percent_change_from_baseline),
               name="Grocery and pharmacy", fill='tonexty', mode='none'), row=1, col=2
)


# Top right
fig.add_trace(
    go.Scatter(x=list(mobility_total.date),
               y=list(mobility_total.parks_percent_change_from_baseline),
               name="Parks", fill='tonexty', mode='none'), row=1, col=3
)


# Bottom left
fig.add_trace(
    go.Scatter(x=list(mobility_total.date), y=list(mobility_total.transit_stations_percent_change_from_baseline),
               name="Transit stations", fill='tonexty', mode='none'), row=2, col=1
)

# Bottom mid
fig.add_trace(
    go.Scatter(x=list(mobility_total.date),
               y=list(mobility_total.workplaces_percent_change_from_baseline),
               name="Workplace", fill='tonexty', mode='none'), row=2, col=2
)


# Bottom right
fig.add_trace(
    go.Scatter(x=list(mobility_total.date), y=list(mobility_total.residential_percent_change_from_baseline),
               name="Residental", fill='tonexty', mode='none'), row=2, col=3
)


fig.update_layout(showlegend=False)

fig.update_layout(
    title_text="Google mobility reports from covid-19 pandemic - change from baseline"
)

# Set template
fig.update_layout(
    template="plotly_white"
)

# fig.update_xaxes(matches='x')

fig.show()