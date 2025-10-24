# Auteurs : Malek
#
# TP : TP3
#
# Date : 23/03/2023
#
# Objet : POPULATION DU NORD
#
# État : TP finie

from matplotlib import pyplot as plt
from random import *
import csv 

#QUESTION 2 : à Tester
#Quand on ouvre le fichier, thonny nous oblige a choisir un codage de caratères autre que utf-8.
#Pour résoudre le problème il suffit de choisir l'encodage ISO-8856.

#QUESTION 3 : Choisissez une structure de données contenant toutes les données de ce fichier comprises entre les lignes 36 et 136, et construisez-la.

"""
crée une liste qui va des lignes 8 à 28 incluses,
donne les nombres d’hommes, de femmes et le total par tranches d’âges de cinq ans, la dernière tranche étant 100 ans ou plus.
"""
with open("rp2016_td_pop1B.xls", "r+") as file:
    liste = file.readlines()
    print(liste[35:136])
    
stat_2016 = liste[35:136]

def stat_2016_V2():
    """
    renvoie la liste d'avant sans les tabulations.
    CU : aucun
    valeur de retour : liste 
    """
    res = []
    j = ""
    for i in range(len(stat_2016)) :
        j = stat_2016[i].strip().split('\t')
        res.append(j)
    return res

stat = stat_2016_V2()
        
#QUESTION 4 :
#Est-ce que pour chaque âge, le nombre donné dans la colonne Ensemble est bien la somme des nombres des deux colonnes Hommes et Femmes ?
#Non 

def vérif(l):
    """
    vérifie que la case ensemble est la somme du nombre de femmes et d'hommes.
    param : l (list)
    CU : aucune
    valeur de retour : bool
    exemple :
    >>> vérif(stat)
    False
    """
    res = True
    i = 0
    while i<len(l) and res :
        if int(l[i][1]) + int(l[i][2]) != int(l[i][3]) :
            res = False
        i = i +1
    return res
    
#QUESTION 5 :
#Produire un graphique montrant les nombres d’hommes et de femmes en fonction de leur âge.

def homme (l) :
    res = []
    for i in l :
        res.append(int(i[1]))
    return res

def femme(l):
    res = []
    for i in l :
        res.append(int(i[2]))
    return res

def age(l) :
    res =[]
    for i in l :
        if i[0] != "100 ans ou plus" :
            res.append(i[0])
        else :
            res.append("105 ans")
    return res

def age_ensemble(l):
    res = []
    for i in l :
        res.append(int(i[3]))
    return res

ensemble = age_ensemble(stat)

hommes = homme(stat)
femmes = femme(stat)
ages = age(stat)

#******************Création du graphique*************
fig, ax = plt.subplots()
ax.plot(ages, hommes, label='Hommes')
ax.plot(ages, femmes, label='Femmes')

ax.set_xlabel('Âge')
ax.set_ylabel('Nombre de personnes')
ax.set_title('Répartition des hommes et des femmes en fonction de leur âge')
ax.legend()
#********************Afficher le graphique***************************
#plt.show()

#Question 6 :À la naissance on peut constater qu’il y a plus d’hommes que de femmes,
#et en revanche chez les personnes âgées les femmes sont plus nombreuses. À quel âge l’inversion se fait-elle ?

def inversion () :
    """
    renvoie l'age où l'effectif des femmes et supérieurs a celui des hommes
    param : aucun
    CU : aucun
    valeur de retour : int or float
    """
    res = 0
    i = 0
    while int(hommes[i]) > int(femmes[i]) :
        i = i +1
    return ages[i+1]

#Question 7 :
#Calculez les âges moyens des hommes et des femmes. Pour la tranche d’âge 100 ans et plus vous prendrez un âge commun de 105 ans.

def age_moyen(l):
    """
    renvoie l'age moyen des hommes et des femmes.
    param : l(list)
    CU : aucun
    valeur de retour : int or float
    exemple :
    >>> age_moyen(stat)
    38
    """
    res = 0
    somme = 0
    for i in range (0,len(l)) :
        res = res + i*ensemble[i]
        somme = somme+ ensemble[i]
    return res//somme

#Question 8
def median_hommes():
    """
    renvoie l'age médian des hommes
    param: aucun
    CU : aucun
    valeur de retour : float
    exemple :
    >>> median_hommes()
    36.0
    """
    age = []
    res = 0
    h = []
    x= sum(hommes)
    for i in range(0,len(hommes)):
        age.append(i)
        j = 0
        while j<hommes[i] :
            h.append(i)
            j = j +1
    if x%2 == 0 :
        res = (h[len(h)//2] + h[len(h)//2 - 1])/2
    return res

def median_femmes():
    """
    renvoie l'age médian des femmes
    param: aucun
    CU : aucun
    valeur de retour : int or float
    exemple :
    >>> median_femmes()
    39
    """
    age = []
    res = 0
    h = []
    x= sum(femmes)
    for i in range(0,len(femmes)):
        age.append(i)
        j = 0
        while j<femmes[i] :
            h.append(i)
            j = j +1
    if x%2 == 0 :
        res = (h[len(h)//2] + h[len(h)//2 - 1])/2
    else :
        res =h[len(h)//2]
    return res
    
#QUESTION 9 : Produisez un fichier au format CSV

with open("rp2016_td_pop1B.xls", "r+") as file:
    liste2 = file.readlines()
    
pop_nord_avec_tab = liste2[6:29]

def pop_nord_2016():
    """
    renvoie la liste d'avant sans les tabulations.
    CU : aucun
    valeur de retour : liste 
    """
    res = []
    j = ""
    for i in range(len(pop_nord_avec_tab)) :
        j = stat_2016[i].strip().split('\t')
        res.append(j)
    return res

pop_nord = pop_nord_2016()

question9 = "population_nord_2016_par_cinq_ans.csv"

"""
crée le fichier csv 
"""

with open('rp2016_td_pop1B.xls','r') as file :
    l = file.readlines()
popnord = l[8:28]


with open('fichier.csv','w+') as filecsv :
    writer = csv.writer(filecsv,delimiter=",")
    writer.writerow(["Année", "Âge", "Hommes", "Femmes"])
    for i in popnord :
        writer.writerow([i["Année"], i["Âge"], i["Hommes"], i["Femmes"]])



if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
