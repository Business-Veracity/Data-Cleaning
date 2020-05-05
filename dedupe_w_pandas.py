import pandas as pd

toclean = pd.read_csv('ia_summary.csv')
deduped = toclean.drop_duplicates(['id'])
deduped.to_csv('myfilewithoutduplicates.csv')