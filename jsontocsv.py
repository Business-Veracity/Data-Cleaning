import pandas as pd
df=pd.read_json('1gig.json')
df.to_csv('largeloadme.csv')
