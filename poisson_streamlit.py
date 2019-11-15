import holoviews as hv
import hvplot.pandas
import numpy as np
import pandas as pd
from scipy.stats import poisson
import streamlit as st

hv.extension('bokeh')


st.title('Visualizing Poisson Distributions using Streamlit')

mu = st.slider(
    'Choose mean of poisson distribution:',
    value=2.0,
    min_value=0.0,
    max_value=10.0,
    step=0.25,
)

x_values = np.arange(0, 100)
probabilities = poisson.pmf(k=x_values, mu=mu)

df = pd.DataFrame({
    'x': x_values,
    'probabilities': probabilities,
})

df_subset = df[(df.x <= 20) | (df.x <= mu * 3)]

plot = df_subset.hvplot(
    kind='bar',
    y='probabilities',
    xlabel='X = x',
    ylabel='P(X = x)',
)

st.write(hv.render(plot))
