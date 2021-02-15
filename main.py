def dessinPendu(nb):
    tab = [
        """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
        """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]


# test = dessinPendu()
# print(test)

motRechercher = "salut"

nbError = 0
lettreCorrect = 0
lettreRegister = []
tailleMot = len(motRechercher)
motUndefined = "_"*tailleMot
mot = list(motUndefined)
defaite = 1

while nbError < 6:
    lettreCorrect = 0
    saisieChar = input("Saisir un caractère \n")
    for i in motRechercher:
        if saisieChar == i:
            lettreRegister.append(i)
            lettreCorrect = 1

    if (lettreCorrect == 1):
        print("Vous avez trouvez une bonne lettre")
        print(lettreRegister)
        print(dessinPendu(nbError))

    else:
        print("Vous avez réaliser une erreur")
        nbError = nbError + 1
        print(dessinPendu(nbError))

    emplacementChar = any
    for i in motRechercher:
        for char in lettreRegister:
            if i == char:
                emplacementChar = motRechercher.find(i)
                mot[emplacementChar] = i

    print(''.join(mot))

    test = ''.join(mot)
    if(test == motRechercher) :
        print("Vous avez Gagner")
        defaite = 0

if defaite == 1 :
    print("Vous avez perdu !")