import ujson as json
import pandas as pd

records = map(json.loads, open('15.json'))
df = pd.DataFrame.from_records(records)

df.to_csv(r'transformedjason.csv', index = False)
