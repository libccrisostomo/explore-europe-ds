import plotly.graph_objects as go # or plotly.express as px

import plotly.express as px
from process_data import *
import dash
import dash_core_components as dcc
import dash_html_components as html

fig_eu = px.sunburst(df_eu, path=['Country', 'City'], width=800, height=800)
fig_pt = px.sunburst(df_pt, path=['Country', 'City'], width=500, height=500)

app = dash.Dash()
app.layout = html.Div([
    # dcc.Graph(figure=fig_eu),
    html.Div([
        html.Div([
            # html.H3('Column 1'),
            dcc.Graph(figure=fig_pt)
        ], className="six columns"),

        html.Div([
            html.H3('Column 2'),
            dcc.Graph(figure=fig_pt)
        ], className="six columns"),
    ], className="row")
])
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

#
# app.layout = html.Div([
#     dcc.Graph(figure=fig_eu),
#     dcc.Graph(figure=fig_pt)
# ])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter