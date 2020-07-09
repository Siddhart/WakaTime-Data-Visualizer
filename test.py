import os
import json
import math
import matplotlib.pyplot as plt
import numpy as np

with open("./input/data.json") as json_file:
    data = json.load(json_file)


#here
Editors = []
Amount = []
total = []
for i in range(len(data["days"])):
    temp = len(data["days"][i]["editors"])  
    for x in range(temp):
        name = data["days"][i]["editors"][x]["name"]
        total.append(name)
        if name not in Editors:
            Editors.append(name)
    
for i in range(len(Editors)): 
    EditorName = (Editors[i])
    temptemp = 0
    for f in range(len(total)):
        tempName = (total[f])
        if EditorName == tempName:
            temptemp +=1
    Amount.append(temptemp)

patches, texts = plt.pie(Amount, startangle=90)
plt.legend(patches, Editors, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()

#here