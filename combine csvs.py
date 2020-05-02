import os, glob
import pandas as pd

#combine
path = "/home/daniel/Data/csv4upoload"

all_files = glob.glob(os.path.join(path, "04*.csv"))
print(all_files)
combined_csv = pd.concat( [pd.read_csv(f) for f in all_files ] )
combined_csv.to_csv("merged.csv", index=False, encoding="utf-8")
combined_csv.info()

#DeDupe
#d = pd.read_csv('merged.csv', keep_default_na = False, )
#d['agentid'] = d['agentid'].astype('int')
#d.drop_duplicates(subset = ['id', 'agentid', 'duration'], inplace = True, keep = 'first')
#d.to_csv('mergededuped.csv', index = False, encoding="utf-8")
#mergededuped.csv.info()

