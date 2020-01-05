import pandas as pd
def Pandas(url):
    file = pd.read_csv(url, sep=",")
    s = [list(file.loc[i]) for i in range(len(file["ФИО"]))]  # todo: Может по другому len делать? (C)Даня
    d = {s[i][0]: s[i][1:] for i in range(len(s))}
    return d