import plotly.express as px
import plotly.io as pio
from process_data import *

fig_eu = px.sunburst(df_eu, path=['Country', 'City'])
fig_eu.show()

fig_pt = px.sunburst(df_pt, path=['Country', 'City'])
fig_pt.show()

fig_de = px.sunburst(df_de, path=['Country', 'City'])
fig_de.show()