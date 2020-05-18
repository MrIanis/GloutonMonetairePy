# Algorithme glouton de résolution de monnaie à rendre
# A CORRIGER
# NF.NSI

# montant de la monnaie a rendre
montant = 1.65

# valeur des pieces disponibles en euro trié dans l'ordre croissant
pieces = [ 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]

## exemple de cas non optimal
## montant = 21
## pieces = [ 18, 7, 1 ]

def Monnaie(somme, ListeMontants):

    # tableau de nombre de piece max a rendre selon le tableau de pieces
    ListeNbPiece=[-1] 
    
    for i in ListeMontants:

    # parcours de la liste des pieces
        for k in range(len(ListeMontants)):

            # recupere le nombre de piece selon le quotient (entier //)
            ListeNbPiece[k]=somme//ListeMontants[i]

            # somme restante a deduire du montant
            somme==round(somme%ListeMontants[k], 2)

    return somme,ListeNbPiece

print (Monnaie(montant,pieces))
