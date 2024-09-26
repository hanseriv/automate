"""
auteur : jean TROUSSIER
date : 26 sept 2024
objectif : fichier contenant les test du programme
"""
import test_function as tf
#test qui doivent être vrai
print("test qui sont vrai")
print(tf.bool_test_algo("le joli chat mange.")) 
print(tf.bool_test_algo("le ,joli chat ; dort."))
print(tf.bool_test_algo("la grosse souris verte mange le joli petite chat blanc."))
print(tf.bool_test_algo("la grosse souris verte mange jean."))
print(tf.bool_test_algo("Jean dort."))
print(tf.bool_test_algo("Jean mange Martin."))
print(tf.bool_test_algo("Jean mange le chat."))
print(tf.bool_test_algo("la verte souris grosse petit mange le bleu verte chat petite."))
print("test qui doivent return false")
print(tf.bool_test_algo("."))
print(tf.bool_test_algo(""))
print(tf.bool_test_algo("le jolichat joue"))
print(tf.bool_test_algo("le joli chat joue."))