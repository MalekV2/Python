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


from ap2_decorators import count
#nombre de fibonacci
# f(0)=0
# f(1)=1
# f(2)=1
# f(3)=2
# f(4)=3
# f(5)=5
# f(6)=8
# f(7)=13
# f(8)=21
# f(9)=34
# f(10)=55
@count
def fibo(n):
    """
    n passé en paramètre renvoie le terme f(n)de la suite de Fibonacci
    parametre:n (int)
    valeurs de retour: int
    CU:n>=0
    >>> fibo(5)
    5
    >>> fibo(4)
    3
    >>> fibo(6)
    8
    """
    if n==0:
        res=0
    elif n==1:
        res=1
    else:
        res=(fibo(n-1)+fibo(n-2))
    return res

# f(40)=102334155
# l'ordinateur prends du temps a le réaliser

#fibo(0)=0
#fibo.counter=1
# f(1)=1
#fibo.counter=1
# f(2)=1
#fibo.counter=3
# f(3)=2
#fibo.counter=5
# f(4)=3
#fibo.counter=9
# f(5)=5
#fibo.counter=15
# f(6)=8
#fibo.counter=25
# f(7)=13
#fibo.counter=41
# f(8)=21
#fibo.counter=67
# f(9)=34
#fibo.counter=109
# f(10)=55
#fibo.counter=177
#fibo(40)=102334155
#fibo.counter= 331160281

if __name__ == '__main__':
   import doctest
   doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)

