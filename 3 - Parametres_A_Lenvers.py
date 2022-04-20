def Parametres_A_Lenvers(*mots):
    mots_a_lenvers=[]
    
    for i in range(len(mots)):
        if type(mots[i]) == int:
            print("ERREUR: Il ne faut pas entrer de chiffres")
            return

    if len(mots) < 2:
        print("ERREUR: Il faut passer au moins deux arguments")
        return

    elif len(mots) == 0:
        print("ERREUR: Il faut passer au moins deux arguments")
        return
    for mot in mots:
        mots_a_lenvers.append(mot)
    print(" ".join(mots_a_lenvers[::-1]))

Parametres_A_Lenvers("Suis", "Je", "Drole")