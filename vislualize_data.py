import plotly.express as px
import plotly.io as pio
from process_data import *

fig = px.sunburst(df, path=['Country', 'City'])
fig.show()