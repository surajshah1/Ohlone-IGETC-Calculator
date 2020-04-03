#Patented IGETC Algorithm
import xlrd
import sys
import json

#TODO: remove button
path = "book.xlsx"
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

inputClassesTaken = str(sys.argv[1])
inputClassesTaken = json.loads(inputClassesTaken)
ICT = inputClassesTaken[:]
print(ICT)
#print(" script input: ", inputClassesTaken)

#python dictionary for all the classes
igetcAreas = {"area1": [], "area2" : [], "area3a": [], "area3b": [], "area4": [], "area5alab": [], "area5blab":[],"area5aNon":[],"area5bNon":[], "area6":[], "areaUCA":[]}
igetcCoursesLeft = {"area1": 0, "area2" : 0, "area3" : 0, "area3a": 0, "area3b": 0, "area4": 0, "area5alab": 0, "area5blab":0,"area5aNon":0,"area5bNon": 0, "area6": 0, "areaUCA": 0}
#loops that take the spredsheet values and assign put it in the python dictionary
for x in range(1,4):
    igetcAreas["area1"].append(inputWorksheet.cell_value(x,0))

for x in range(1,9):
    igetcAreas["area2"].append(inputWorksheet.cell_value(x,1))

for x in range(1,25):
    igetcAreas["area3a"].append(inputWorksheet.cell_value(x,2))

for x in range(1,62):
    igetcAreas["area3b"].append(inputWorksheet.cell_value(x,3))

for x in range(1,65):
    igetcAreas["area4"].append(inputWorksheet.cell_value(x,4))

for x in range(1,22):
    igetcAreas["area5alab"].append(inputWorksheet.cell_value(x,5))

for x in range(1,9):
    igetcAreas["area5aNon"].append(inputWorksheet.cell_value(x,6))

for x in range(1,11):
    igetcAreas["area5blab"].append(inputWorksheet.cell_value(x,7))

for x in range(1,6):
    igetcAreas["area5bNon"].append(inputWorksheet.cell_value(x,8))

for x in range(1,26):
    igetcAreas["area6"].append(inputWorksheet.cell_value(x,9))

for x in range(1,14):
    igetcAreas["areaUCA"].append(inputWorksheet.cell_value(x,10))


#print(igetcAreas)
#function that compares the input to the course list
def compareClasses(inputClassesTaken):
    """
    Input classes and compare to lists of classes in area to output list of classes required in each area
    """
    areasWithCourses = {}

    areasWithCourses["Area 1: English Communication (" + str(igetcCoursesLeft["area1"]) + " courses left for CSU, " + str(igetcCoursesLeft["area1"] - 1) + " for UC)"] = completeEnglish(ICT)
    print("ICT", ICT)
    areasWithCourses["Area 2: Mathematical Concepts and Quantitative Reasoning (1 course left)"] = completeMath(ICT)
    print("ICT 2", ICT)
    artsAndHumanities = completeArtsAndHumanities(ICT)
    areasWithCourses["Area 3: Arts and Humanities (1 course left)"] = artsAndHumanities[2]
    areasWithCourses["Area 3A: Arts (1 course left)"] = artsAndHumanities[0]
    areasWithCourses["Area 3B: Humanities (1 course left)"] = artsAndHumanities[1]
    areasWithCourses["Area 4: Social and Behavioral Science (" + str(igetcCoursesLeft["area4"]) + " courses left)"] = completeSocialAndBehavioralSciences(ICT)
    areasWithCourses["Area 5A: Physical Science (1 course left)"] = completePhysicalAndBiologicalSciences(ICT)[0]
    areasWithCourses["Area 5B: Biological Science (1 course left)"] = completePhysicalAndBiologicalSciences(ICT)[1]
    areasWithCourses["Area 6: Language other than English (1 courses left)"] = completeLanguage(ICT)
    areasWithCourses["US History, Constitution, and American Ideals (CSU required only) (" + str(igetcCoursesLeft["areaUCA"]) + " courses left)"] = completeHistory(ICT)
    output = {}
    for area in areasWithCourses:
        if areasWithCourses[area]:
            output[area] = areasWithCourses[area]
    return output


def completeEnglish(inputClassesTaken):
    counter = 0
    englishCourses = igetcAreas["area1"]
    for inputCourse in inputClassesTaken:
       if inputCourse in igetcAreas["area1"]:
           counter += 1
           englishCourses.remove(inputCourse)
           if inputCourse in ICT:
                print("removed from global")
                ICT.remove(inputCourse)
    if counter >= 2:
        return []
    else:
        igetcCoursesLeft["area1"] = 3 - counter
        return englishCourses

def completeMath(inputClassesTaken):
    mathCourses = igetcAreas["area2"]
    for inputCourse in inputClassesTaken:
        if inputCourse in mathCourses:
            if inputCourse in ICT:
                ICT.remove(inputCourse)
            return []
    return mathCourses

def completeArtsAndHumanities(inputClassesTaken):
    # user must take one class from arts one class from humanites and an extra class from either area
    # ... total of 3 classes in area 3
    arts = igetcAreas["area3a"]
    humanities = igetcAreas["area3b"]
    aCounter = 0
    hCounter = 0
    for inputCourse in inputClassesTaken:
        if inputCourse in igetcAreas["area3a"]:
            aCounter += 1
            if inputCourse in ICT:
                ICT.remove(inputCourse)
            arts.remove(inputCourse)
        elif inputCourse in igetcAreas["area3b"]:
            hCounter += 1
            if inputCourse in ICT:
                ICT.remove(inputCourse)
            humanities.remove(inputCourse)
    if aCounter == 0 and hCounter == 0:
        return [arts, humanities, arts + humanities]
    elif aCounter == 1 and hCounter == 0:
        return [[],humanities, arts + humanities]
    elif aCounter == 0 and hCounter == 1:
        return [arts,[] , arts + humanities]
    elif aCounter == 1 and hCounter == 1:
        return [[],[], arts + humanities]
    elif aCounter == 2 and hCounter == 0:
        return [arts, [], []]
    elif aCounter == 0 and hCounter == 2:
        return [[], humanities, []]
    else:
        return [[],[],[]]



def completeSocialAndBehavioralSciences(inputClassesTaken):
    """
    user must take atleast 3 courses from 2 different disciplines
    there are 16 diffrent disciplines
    2 courses can be from 1 discipline and 1 course can be from another ... 2 1 / 1 2
    3 course each from 3 different disciplines ... 1 1 1
    """
    newList = []
    for inputCourse in inputClassesTaken:
        if inputCourse in igetcAreas["area4"]:
            newList.append(inputCourse)

    socialScience = igetcAreas["area4"]
    disciplineList = {"AJ ": 0,"ANTH": 0,"BA ": 0,"BRDC": 0,"CHS": 0,"COMM": 0, "ECS": 0,"ENVS": 0,"GEOG": 0,"HIST": 0,"IS ": 0,"JOUR": 0,"PS ": 0,"PSY": 0,"SOC": 0,"WS ": 0}
    for i in newList:
        for d in disciplineList:
            if i[:3] == d[:3]:
                disciplineList[d] += 1
            if disciplineList[d] > 2:
                for course in socialScience:
                    if course[:3] == d[:3]:
                        if inputCourse in ICT:
                            ICT.remove(inputCourse)
                        socialScience.remove(course)
        try:
            socialScience.remove(i)
        except ValueError:
            pass

    dcounter = 0
    tcounter = 0
    for d in disciplineList:
        if disciplineList[d]:
            dcounter += 1
            tcounter += disciplineList[d]
    if dcounter >= 2 and tcounter >= 3:
        return []
    else:
        igetcCoursesLeft["area4"] = 3 - tcounter
        return socialScience


def completePhysicalAndBiologicalSciences(inputClassesTaken):
    aLab = igetcAreas["area5alab"]
    bLab = igetcAreas["area5blab"]
    aNon = igetcAreas["area5aNon"]
    bNon = igetcAreas["area5bNon"]
    alcomplete = False
    blcomplete = False
    ancomplete = False
    bncomplete = False
    aLab = [course for course in aLab if course not in aNon]
    newList = []
    for inputCourse in inputClassesTaken:
        if (inputCourse in aLab) or (inputCourse in bLab) or (inputCourse in aNon) or (inputCourse in bNon):
            newList.append(inputCourse)
    for course in newList:
        if course in aLab:
            alcomplete = True
        if course in bLab:
            blcomplete = True
        if course in aNon:
            ancomplete = True
        if course in bNon:
            bncomplete = True
    if not alcomplete and not blcomplete and not ancomplete and not bncomplete:
        return [aLab + aNon, bLab + bNon]
    elif not alcomplete and not blcomplete and ancomplete and not bncomplete:
        return [[], bLab]
    elif not alcomplete and not blcomplete and not ancomplete and bncomplete:
        return [aLab, []]
    elif  alcomplete and not blcomplete and not ancomplete and not bncomplete:
        return [[], bLab + bNon]
    elif not alcomplete and blcomplete and not ancomplete and not bncomplete:
        return [aNon + aLab, []]
    elif not alcomplete and not blcomplete and ancomplete and bncomplete:
        return [aLab, bLab]
    else:
        return [[],[]]

def completeLanguage(inputClassesTaken):
    language = igetcAreas["area6"]
    for inputCourse in inputClassesTaken:
        if inputCourse in language:
            if inputCourse in ICT:
                ICT.remove(inputCourse)
            return []
    return language

def completeHistory(inputClassesTaken):
    history = igetcAreas["areaUCA"][:]
    history.remove("PS 102")
    history.remove("HIST 105")
    part1 = False
    part2 = False
    part3 = False
    part4 = False
    counter = 2

    if "HIST 117A" in inputClassesTaken or "HIST 117B" in inputClassesTaken:
            part1 = True
            counter = 1
    if "HIST 105" in inputClassesTaken or "PS 102" in inputClassesTaken:
            part2 = True
            counter = 1
    if "PS 102" in inputClassesTaken:
            part3 = True
            counter = 1
    for inputCourse in inputClassesTaken:
        if inputCourse in history:
            part4 = True
            counter = 1
    if (part1 and part2) or (part3 and part4):
        counter = 0
        return []
    igetcCoursesLeft["areaUCA"] = counter
    return igetcAreas["areaUCA"]

x = compareClasses(inputClassesTaken)

with open('outputclasses.json', 'w') as fp:
    json.dump(x, fp)

# print courses at the bottom
