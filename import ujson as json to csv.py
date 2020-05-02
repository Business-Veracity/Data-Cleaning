import ujson as json
import pandas as pd

records = map(json.loads, open('trasnformme.json'))
df = pd.DataFrame.from_records(records)
#df["duration"]= df["duration"].astype(float) 
df.to_csv(r'transformedjasonlgdm.csv', index = False, encoding="utf-8")
print (df.dtypes)
