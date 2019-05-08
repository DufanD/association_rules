import csv
import numpy as np
import pandas as pd
from apyori import apriori
import pprint

store_data = list()
with open('data/supermarket_goods.csv', 'r') as csvFile:
  reader = csv.reader(csvFile)
  for read_item in reader:
    store_data.append(read_item)
csvFile.close()

association_rules = list(apriori(store_data, min_support=0.3, min_confidence=0.8))
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