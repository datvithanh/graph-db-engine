import numpy as np
import pandas as pd
import json
from nodes import Food, Nutrition
df = pd.read_csv('data/food_nutritions.csv')
col_list = ['NameEng', 'NameVn', 'Nutritions']
nparr = np.array(df[col_list])

for x in nparr:
    try:
        x[2] = json.loads(x[2].replace('"', '"'))
    except:
        print(x[2])
nutris = set()
for x in nparr:
    nutris = nutris.union(set(x[2].keys()))

nutris_node = {}
food_node = {}
for nutri in nutris:
    nutris_node[nutri] = Nutrition(name=nutri).save()

for x in nparr:
    food_node[x[0]] = Food(name_en = x[0], name_vi = x[1]).save()
    for k,v in x[2].items():
        if float(v.split(' ')[0]) > 0:
            food_node[x[0]].nutritions.connect(nutris_node[k])

# nutris = ['Water','Energy','Prottein','Fat','Carb','Fiber','Sugars','Calcium','Iron_Fe','Magne_Mg','Potassium_K','Sodium_Na','Zinc_Z','Vitamin_C','Vitamin_B6','Vitamin_B12','Vitamin_A','Vitamin_E','Vitamin_D23','Vitamin_D','Cholesterol','Caffein']
# print(len(nutris))