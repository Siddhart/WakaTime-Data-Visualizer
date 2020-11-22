import os
import json
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

line = "--------------------------------------------"


SendDis = """
--------------------------------------------
Total hours spend:
[0] - Get the total number of hours.
[1] - Get a bar graph of the total amount of hours.
[2] - Get a graph with the total amount of hours.
--------------------------------------------
Editors:
[3] - Get all the used editors with their percentage
[4] - Get a pie chart of all the used editors.
[5] - Get a bar chart of all the used editors.
--------------------------------------------
Languages:
[6] - Get a pie chart of all the used Languages.
"""


arr = os.listdir("./input/")
if not arr:
    print("the data file was not found!")
    exit()

fileName = "./input/" + arr[0]

with open(fileName) as json_file:
    data = json.load(json_file)


#0
def GetHours():
    HOURS = 0.0
    MINUTES = 0.0
    for i in range(len(data["days"])):
        HOURS += int(data["days"][i]["grand_total"]["hours"])
        MINUTES += float(data["days"][i]["grand_total"]["minutes"])

    HOURS += (math.floor(MINUTES/60))
    print("Hours: " + str(HOURS))

#1
def BarGraph():
    Days = []
    HoursPerDay = []

    for i in range(len(data["days"])):
        temp = 0
        Days.append(int(i))
        temp += int(data["days"][i]["grand_total"]["hours"])
        temp += (math.floor(float(data["days"][i]["grand_total"]["minutes"]) /60))
        HoursPerDay.append(float(temp))

    plt.bar(Days, HoursPerDay, 
        width = 0.8, color = ['green', 'green']) 
    plt.ylabel("Hours")
    plt.xlabel("Days") 

    what = str(input("Do you want to save this? (y/n): ")).lower()
    if what == "y":
        name = str(input("Enter the name for the file: "))
        plt.savefig("./output/" + name)
        print("File saved!")
    plt.show()

#2
def MakeGraph():
    Days = []
    HoursPerDay = []

    for i in range(len(data["days"])):
        temp = 0
        Days.append(int(i))
        temp += int(data["days"][i]["grand_total"]["hours"])
        temp += (math.floor(float(data["days"][i]["grand_total"]["minutes"]) /60))
        HoursPerDay.append(float(temp))

    plt.plot(Days, HoursPerDay)
    plt.ylabel("Hours")
    plt.xlabel("Days")

    what = str(input("Do you want to save this? (y/n): ")).lower()
    if what == "y":
        name = str(input("Enter the name for the file: "))
        plt.savefig("./output/" + name)
        print("File saved!")
    plt.show()

#3
def GetEditors():
    Editors = []
    Amount = []
    total = []
    totaldays = len(data["days"])
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
    
    FinalString = ""
    for i in range(len(Editors)):
        FinalString += str(Editors[i] +": " + str(round(Amount[i] / totaldays * 100,2)) + "%\n")
    
    print(FinalString)


#4
def MakePieChart():
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
    plt.legend( loc = 'right', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(Editors, Amount)])
    plt.axis('equal')
    plt.tight_layout()   

    what = str(input("Do you want to save this? (y/n): ")).lower()
    if what == "y":
        name = str(input("Enter the name for the file: "))
        plt.savefig("./output/" + name)
        print("File saved!")
    plt.show()

#5
def MakeBarChart():
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

    x = np.arange(len(Editors))
    fig, ax = plt.subplots()
    plt.bar(x, Amount)
    plt.xticks(x, Editors)

    what = str(input("Do you want to save this? (y/n): ")).lower()
    if what == "y":
        name = str(input("Enter the name for the file: "))
        plt.savefig("./output/" + name)
        print("File saved!")

    plt.show()

#6
def GetLanguagePieChart():
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
    what = str(input("Do you want to save this? (y/n): ")).lower()
    if what == "y":
        name = str(input("Enter the name for the file: "))
        plt.savefig("./output/" + name)
        print("File saved!")

    plt.show()

#7
def GetLanguageText():
    print("Work on dis")
    
print(SendDis)
inp = int(input("Enter the index of your choice: "))

if (inp == 0):
    GetHours()
elif (inp == 1):
    BarGraph()
elif (inp == 2):
    MakeGraph()
elif (inp==3):
    GetEditors()
elif (inp==4):
    MakePieChart()
elif (inp==5):
    MakeBarChart()
elif (inp==6):
    GetLanguagePieChart()
elif (inp==6):
    GetLanguageText()