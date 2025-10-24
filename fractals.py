# Auteurs : Houhou Abdel-malek Sottile Lorenzo
#
# TP : TP2 
#
# Date : 08/02/2023
#
# Objet : Algorithmes récursifs
#
# État : description détaillée de l'état d’avancement du TP :
#        - fonctions réalisées correctement
#        - fonctions non achevées
#        - remarques éventuelles
#        - ...


import turtle

# Dessins de fractales

# turtle.setheading(45)
# turtle.backward(80)
# turtle.setheading(-45)
# turtle.backward(80)
# turtle.setheading(45)
# turtle.backward(80)
# turtle.setheading(-45)
# turtle.backward(80)
# turtle.setheading(45)
# turtle.backward(80)
# turtle.setheading(-45)
# turtle.backward(80)
# turtle.setheading(45)
# turtle.backward(80)
# turtle.setheading(45)

#Question
#la relation qu'il y a entre la longueur de tracé l à l’ordre n et à l’ordre n+1
#est une relation de 4/3


def von_koch(n,l):
    """
    dessine une partie du flocon de Von Koch
    parametre: n(int),l(int)
    valeurs de retour: fonction
    CU: les entiers ne doivent pas etre négatif
    """

    if n==0:
        turtle.forward(l)
    else:
        turtle.speed(75)
        von_koch(n-1,l/3)
        turtle.left(60)
        von_koch(n-1,l/3)
        turtle.right(120)
        von_koch(n-1,l/3)
        turtle.left(60)
        von_koch(n-1,l/3)
        



def tout_le_flocon(n,l):
    """
    trace le flocon de von koch de longeur et de niveau d'iteration n
    parametre: n(int),l(int)
    valeurs de retours: fonction
    """
    for i in range(3):
        von_koch(n,l)
        turtle.right(120)


#courbe de cesaro
# a l'ordre n+1 la longeur du tracé revient a la longeur du trace n divisé par 2

def cesaro(n,l):
    """
    trace une partie de carré de cesaro de longeur l et d'iteration n
    parametre: n(int) , l(int)
    valeurs de retour: fonction
    """
    if n==0:
        turtle.forward(l)
    else:
        cesaro(n-1,l/2)
        turtle.left(85)
        cesaro(n-1,l/2)
        turtle.right(170)
        cesaro(n-1,l/2)
        turtle.left(85)
        cesaro(n-1,l/2)
        
def carré_de_cesaro(n,l):
    """
    trace la totalité du carré de cesaro de longueur l d'iteration n
    parametre: n(int), l(int)
    valeurs de retour: fonction
    """
    for i in range (4):
        cesaro(n,l)
        turtle.left(90)
        
#Triangle de Sierpinski
#question a faire
#longueur est divisé par 2
#à réaliser
def sierpinski(n,l):
    """
    trace le triangle de sierpinski de longeur l d'iteration n
    parametre:
    l,int la longeur
    n,int iteration
    valeurs de retour:
    fonction
    """
    turtle.speed(100)
    if n==0:
        for i in range(3):
            turtle.forward(l)
            turtle.left(120)
    else:
        for i in range(3):
            sierpinski(n-1,l/2)
            turtle.forward(l)
            turtle.left(120)
            
            
            
            
            

if __name__ == '__main__':
   import doctest
   doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)