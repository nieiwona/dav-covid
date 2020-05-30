import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objects as go

data_tests = pd.read_csv('./../data/Australia-COVID-Data.csv')
data_cases = pd.read_csv('./../data/aus_covid_data.csv')
data_world = pd.read_csv('./../data/covid_19_clean_complete.csv')
cases_rage = data_cases[27:146]
cases_daily = cases_rage['new_cases'].tolist()
data_tests['cases_daily'] = cases_daily
aus_jurisdictions = data_world.loc[data_world['Country/Region'] == 'Australia']
jurisdictions_dates = aus_jurisdictions[24:976]
jurisdictions_droped = jurisdictions_dates.drop(['Country/Region', 'Lat', 'Long', 'Date', 'Deaths', 'Recovered'], 1)
jurisdictions_grouped = jurisdictions_droped.groupby('Province/State').aggregate(lambda tdf: tdf.unique().tolist())
print(jurisdictions_grouped)
# jurisdictions_transposed = jurisdictions_grouped.T
# print(jurisdictions_grouped)

# Create figure with secondary y-axis
# fig = make_subplots(specs=[[{"secondary_y": True}]])
#
# fig.add_trace(
#     go.Bar(x=list(data_tests.date), y=list(data_tests.cases_daily),
#            name="New cases"))
#
#
# fig.add_trace(
#     go.Scatter(x=list(data_tests.date), y=list(data_tests.daily), mode='lines+markers', marker_color='rgb(5,255,255)',
#                name="Tests performed", yaxis="y2"))
#
# # Create axis objects
# fig.update_layout(
#     xaxis=dict(
#         domain=[0.7, 0.5]
#     ),
#     yaxis=dict(
#         title="New infections",
#         titlefont=dict(
#             color="#1910d8"
#         ),
#         tickfont=dict(
#             color="#1910d8"
#         ),
#         side='right'
#     ),
#     yaxis2=dict(
#         title="Tests performed",
#         titlefont=dict(
#             color="rgb(5,255,255)"
#         ),
#         tickfont=dict(
#             color="rgb(5,255,255)"
#         ),
#         side="left",
#     )
# )
#
# # Set x-axis title
# fig.update_xaxes(title_text="xaxis title")
#
# # Set title
# fig.update_layout(
#     title_text="New cases of covid-19 and tests performed in Australia daily"
# )
#
# # Set template
# fig.update_layout(
#     template="plotly_white"
# )
#
# fig.update_layout(showlegend=False)
#
# # Add range slider
# fig.update_layout(
#     xaxis=dict(
#         rangeselector=dict(
#             buttons=list([
#                 dict(count=7,
#                      label="1w",
#                      step="day",
#                      stepmode="backward"),
#                 dict(count=14,
#                      label="2w",
#                      step="day",
#                      stepmode="backward"),
#                 dict(count=1,
#                      label="1m",
#                      step="month",
#                      stepmode="backward"),
#                 dict(count=2,
#                      label="2m",
#                      step="month",
#                      stepmode="backward"),
#                 dict(step="all")
#             ])
#         ),
#         rangeslider=dict(
#             visible=True
#         ),
#         type="date"
#     )
# )
#
# fig.show()
