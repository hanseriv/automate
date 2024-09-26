"""
auteur : jean TROUSSIER
date : 26 sept 2024
objectif : ici seront coder toutes les fonction liée a la sasie des informations et du traitements des erreurs li a ceux-ci
"""
def liste_saisie_utilisateur(string_phrase):
    """
    fonction qui prend en entrée une string (string_phrase) est qui la retourne en liste de string 
    """
    liste_string_input =[]
    string_mot = ""
    for lettre_char in string_phrase:
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
    if '.' in liste_string :
        return True
    return False