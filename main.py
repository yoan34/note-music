# le programme doit permettre d'apprendre la distance entre les notes.
# exercice 1: on a une deux note afficher comme 'DO --> RE#' et on doit
# trouver le nombre de demi-ton entre ces deux notes.
# exercice 2: on a deux note afficher comme DO <-- LA et on doit trouver
# le nombre de demi-ton entre ces deux notes.

from utils.view import showView
from tools import analyseInputUser

session = {
    'user': '',
    'path': 'home',
    'start': 0,
    'end': 0,
    'name_exercise': '',
    'question': 0,
    'answer': 0,
    'good_answer': 0,
}



while True:
    
    showView(session)
    
    session['user'] = input('> '.rjust(20))
    if session['user'].upper() == 'Q':
        break

    session = analyseInputUser(session)
