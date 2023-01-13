import os
import time
import inspect
from random import choice
from utils.tools import NOTES

clear = lambda: os.system('clear')

def showView(session):
    dispatcher = {
        'home': home,
        'find_note_positif': find_note_positif,
        'find_note_negatif': find_note_negatif,
        'find_demi_ton_positif': find_demi_ton_positif,
        'find_demi_ton_negatif': find_demi_ton_negatif,
    }
    clear()
    dispatcher[session['path']](session)
        
def home(session):
    print(f"{'exercice guitar':-^60}")
    print('')
    print(f"{'1 - find note positif':>40}")
    print(f"{'2 - find note negatif':>40}")
    print(f"{'3 - find demi-ton positif':>44}")
    print(f"{'4 - find demi-ton positif':>44}")
    print()
    print("-"*60)
        
    
def find_note_positif(session):
    session['start'] = time.time()
    session['name_exercise'] = inspect.stack()[0][3]
    print(f"{'exercice: {}'.format(session['name_exercise']):-^60}")
    note = choice(NOTES)
    demi_ton = choice(list(range(1,12)))
    index_note = NOTES.index(note)
    new_index = (index_note + demi_ton) % 12
    
    question = {
        "note": note,
        "demi_ton": demi_ton,
        "answer": NOTES[new_index],
    }
    print()
    print(f"{' '*14}Trouver: {question['note']} + {question['demi_ton']} demi tons".ljust(20))
    print()
    
    
def find_note_negatif(session):
    pass
    
def find_demi_ton_positif(session):
    pass
    
def find_demi_ton_negatif(session):
    pass
    
    