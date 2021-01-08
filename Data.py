
import pandas as pd

#importing Citites.csv to display on Data Page
df = pd.read_csv('Resources/cities.csv')
df.to_html('data.html', index=False)

table = df.to_html()
print(table)
