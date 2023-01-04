# le programme doit permettre d'apprendre la distance entre les notes.
# exercice 1: on a une deux note afficher comme 'DO --> RE#' et on doit
# trouver le nombre de demi-ton entre ces deux notes.
# exercice 2: on a deux note afficher comme DO <-- LA et on doit trouver
# le nombre de demi-ton entre ces deux notes.

from utils.view import showView
from tools import analyseInputUser

user = ''
PATH = 'home'
session = {}



while True or user.upper() != 'Q':
    
    showView(PATH, session)
    
    user = input()
    
    analyseInputUser(session)
