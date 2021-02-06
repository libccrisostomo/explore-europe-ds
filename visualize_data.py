import plotly.express as px
from process_data import *

fig_eu = px.sunburst(df_eu, path=['Country', 'City'])
fig_eu.show()

fig_pt = px.sunburst(df_pt, path=['Country', 'City'])
fig_pt.show()

fig_de = px.sunburst(df_de, path=['Country', 'City'])
fig_de.show()

fig_nl = px.sunburst(df_nl, path=['Country', 'City'])
fig_nl.show()

fig_at = px.sunburst(df_at, path=['Country', 'City'])
fig_at.show()

fig_irl = px.sunburst(df_irl, path=['Country', 'City'])
fig_irl.show()
