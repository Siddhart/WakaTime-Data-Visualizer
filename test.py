import os
import json
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

with open("./input/data.json") as json_file:
    data = json.load(json_file)

Languages = []
Amount = []
total = []
for i in range(len(data["days"])):
    temp = len(data["days"][i]["languages"])  
    for x in range(temp):
        name = data["days"][i]["languages"][x]["name"]
        total.append(name)
        if name not in Languages:
            Languages.append(name)
    
for i in range(len(Languages)): 
    EditorName = (Languages[i])
    temptemp = 0
    for f in range(len(total)):
        tempName = (total[f])
        if EditorName == tempName:
            temptemp +=1
    Amount.append(temptemp)

patches, texts = plt.pie(Amount, startangle=90)
plt.legend( loc = 'right', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(Languages, Amount)])
plt.axis('equal')
plt.tight_layout()
plt.show()

print(Languages)
print(Amount)