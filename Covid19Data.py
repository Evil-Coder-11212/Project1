import pandas as pd
import plotly.express as px

df = pd.read_csv("./Covid 19 Data.csv")

fig = px.line(df, x="date", y="cases", color="country", title="Covid 19 Cases each year")

fig.show()