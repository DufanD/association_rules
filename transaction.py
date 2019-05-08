import csv
import numpy as np
import pandas as pd
from apyori import apriori
import pprint

data = pd.read_csv('data/transaction_data_custom.csv', header=None)
data = np.array(data)
data = pd.DataFrame({
        'transaction': data[:, 2],
        'label': data[:, 3],
       })

data_grouped = data.groupby('transaction')
store_data = list()
for key, item in data_grouped:
    store_data.append(item['label'].values.tolist())

association_rules = list(apriori(store_data, min_support=0.1, min_confidence=0.3))
pprint.pprint(store_data)

print("===============================================")

for item in association_rules:
  pair = item[0] 
  items = [x for x in pair]
  if len(items) < 2 :
    print("Rule: " + items[0], end = "")
  else :
    print("Rule: " + items[0], end = "")
    for rule_item in items[1:]:
      print(" -> " + rule_item, end = "")
  print("\nSupport: " + str(item[1]))
  print("Confidence: " + str(item[2][0][2]))
  print("=====================================")