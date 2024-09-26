"""
auteur : jean TROUSSIER
date : 26 sept 2024
objectif : ici seront coder toutes les fonctions prenant lié au traitement des donnée saisie et vérifié
"""
mat_int_etat = [[1,8,8,8,4,8],[8,1,3,8,8,8],[8,2,8,3,8,8],[5,8,8,8,7,9],[8,8,8,3,8,8],[8,5,6,8,8,8],[8,6,8,8,8,9],[8,8,8,8,8,9]]
adj



def int_list_nombre_associé(list_string):
    """
    input : list_string
    output : list_int
    fonction qui retourne une liste de int contenant les valeur associer aux nature de chaque mot de la liste de mot
    """


def bool_etat_de_la_phrase(list_int_indice_mot):
    """
    input : list_int_indice_mot
    output : True/False
    fonction de vérification de l'ordre des mots
    """
    int_cas = 0
    for int_valeur in list_int_indice_mot:
        int_cas = mat_int_etat[int_cas][int_valeur]
        if int_cas == 8:
            return False
        if int_cas == 9:
            return True
    print("error during runtime please notify yourself to the previous programmer")
    return False