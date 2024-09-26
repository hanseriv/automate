"""
auteur : jean TROUSSIER
date : 26 sept 2024
objectif : ici seront coder toutes les fonction liée a la sasie des informations et du traitements des erreurs li a ceux-ci
"""

def liste_phrase_spliter(string_phrase_input):
    """
    fonction qui prend en entrée une string (string_phrase_input)) est qui la retourne en liste de string 
    """
    liste_string_input = []
    string_mot = ""
    for lettre_char in string_phrase_input:
        if lettre_char != " ":
            string_mot += lettre_char 
        else :
            if string_mot != "":
                liste_string_input.append(string_mot)
            string_mot = ""
    if string_mot != "":
        liste_string_input.append(string_mot)
    return liste_string_input


def bool_phrase_vide(liste_string):
    """
    fonction qui prend pour entrée une liste de string (liste_string) et qui retourne True si la matrice est vide ou False dans le cas contraire
    """
    if liste_string == []:
        return True
    return False


def bool_point_checker(liste_string):
    """
    fonction qui vérifie la présence du caractère '.' dans la liste d'entrée (liste_string) et retourne True si la liste contient ce dit caractère 
    ou false le cas échéant
    """
    for string in liste_string :
        if '.' in string :
            return True
        return False

def int_index_word_with_point(list_string):
    """
    input : list_string
    output : unsigned_int_indice 
    fonction qui retourne l'indice du mot contenant le point
    """ 
    unsigned_int_indice = 0
    for string_mot in list_string :
        if '.'  in string_mot :
            return unsigned_int_indice
        else:
            unsigned_int_indice += 1

def string_point_seperator(liste_string):
    """
    input : liste_string
    output : liste_string
    fonction qui supprime tous les mot après le mot contenant le point 
    """
    liste_string = liste_string[ : int_index_word_with_point(liste_string) + 1 : ]
    return liste_string
    

def string_final_point_separator(liste_string):
    """
    input : liste_string
    output : liste_string
    fonction visant a sortir le point du dernier mot
    """
    liste_string[-1] = liste_string[-1][:-1:]
    liste_string.append(".")
    return liste_string