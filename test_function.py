"""
auteur : jean TROUSSIER
date : 26 sept 2024
objectif : fichier contenant les test pour les fonctions
"""
import input_function as ifu
import computing_function as cf

def bool_test_algo(string_phrase):
    list_string_saise = ifu.liste_phrase_spliter(string_phrase)
    if ifu.bool_phrase_vide(list_string_saise) == True:
        print("erreur, votre phrase est fausse")
        return False

    if ifu.bool_point_checker(list_string_saise) == False:
        print("erreur veuiller mettre un point pour signifier la fin de votre phrase")
        return False
    list_string_saise = ifu.string_final_point_separator(ifu.string_point_seperator(list_string_saise))

    list_int_saise = cf.int_list_nombre_associé(list_string_saise)
    if list_int_saise == [1]:
        print("voter mot ne semble pas exister dans nos registre...")
        return False
    if cf.bool_etat_de_la_phrase(list_int_saise) == True:
        print("votre phrase est juste")
        return True
    else:
        print("votre phrase est incorrect")
        return False



