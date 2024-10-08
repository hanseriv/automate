"""
auteur : jean TROUSSIER
date : 26 sept 2024
objectif : ici seront coder toutes les fonctions prenant lié au traitement des donnée saisie et vérifié
To Do : fonction pour ajouter des mots au dictionnaire soi par l'impulsion de l'utilisateur soit en le cherchant sur une bas de donnée plus grande
"""
mat_int_etat = [[1,8,8,8,4,8], #table de transition de l'automate
                [8,1,2,8,8,8],
                [8,2,8,3,8,8],
                [5,8,8,8,7,9],
                [8,8,8,3,8,8],
                [8,5,6,8,8,8],
                [8,6,8,8,8,9],
                [8,8,8,8,8,9]]
dico_de_string = {"petite" : 1,"petit" : 1,"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,"blanc" :1, "mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1, "bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}
list_char_caractere = ['\'',"ß" ,"·", "’", "“", "”", "«", "»", "•", "–", "—", "±", "×", "÷", "²", "³", "€", "†", "‡"]



def int_list_nombre_associé(list_string):
    """
    input : list_string
    output : list_int
    fonction qui retourne une liste de int contenant les valeur associer aux nature de chaque mot de la liste de mot
    """
    list_int = []
    for string_mot in list_string :
        if string_mot not in list_char_caractere:
            if string_mot in dico_de_string:
                list_int.append(dico_de_string[string_mot])
            else :
                print(string_mot)
                print("unrecognise word ")
                return [-1]
    return list_int


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