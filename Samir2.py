import pandas as pd

def f():
    df = pd.read_csv("Humans.csv", sep = ",")
    rooms = pd.read_csv("test15.csv")
    male = []
    place = []
    nomers = []
    boys = 0; girls = 0;
    th = 0
    d = []
    for i in range(len(df["Fios"])):
        mass2 = []
        if df.loc[i][1] == "Male" and df.loc[i][3] == "student":
            boys += 1
        elif df.loc[i][1] == "Female" and df.loc[i][3] == "student":
            girls += 1
        for j in range(len(df.loc[0])):
                mass2.append(df.loc[i][j])
        mass2.append("False")
        male.append(mass2)


    for i in range(len(rooms["places"])):
        d.append([])
        place.append(rooms.loc[i][1])
        nomers.append(rooms.loc[i][0])
        for j in range(place[i]):
            d[i].append([])
    male.sort(key=lambda x: x[2], reverse=True)




    #if boys > girls:

    for i in range(len(place) - 1):
        if place[i] > boys or place[i] == boys and boys != 0:
            for j in range(len(male)):
                if male[j][3] != "teacher" and male[j][1] == "Male":
                    if d[i][-1] != "Male":
                        d[i].append("Male")
                    for l in range(place[i]-1):
                        if d[i][l] == []:
                            if male[j][-1] == "False":
                                d[i][l].append(male[j][0])
                                male[j][-1] = "True"


            for j in range(len(male)):
                if male[j][3] != "teacher" and male[j][1] == "Male":
                    if d[i][-1] != "Male":
                        d[i].append("Male")
                    for l in range(place[i]):
                        if d[i][l] == []:
                            if male[j][-1] == "False":
                                d[i][l].append(male[j][0])
                                male[j][-1] = "True"




    for i in range(len(place)):
        if place[i] > girls or place[i] == girls and girls != 0:
            for j in range(len(male)):
                if male[j][3] != "teacher" and male[j][1] == "Female":
                    if d[i][-1] == "Male":
                        i += 1
                        if d[i][-1] != "Male":
                            d[i].append("Female")
                    for l in range(place[i]):
                        if d[i][l] == []:
                            if male[j][-1] == "False":
                                d[i][l].append(male[j][0])
                                male[j][-1] = "True"





            for j in range(len(male)):
                if male[j][3] != "teacher" and male[j][1] == "Male":
                    for l in range(place[i]):
                        if d[i][l] == []:
                            if male[j][-1] == "False":
                                d[i][l].append(male[j][0])
                                male[j][-1] = "True"
    ans = ''
    for i in range(len(d)):
        for j in range(place[i]):
            ans += str(rooms.loc[i][0]) + " " + str(*d[i][j]) + "\n"
    return ans