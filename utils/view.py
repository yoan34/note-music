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
    if session['question'] is None:
        session = init_question(session)
    if not session['error']:
        session = next_question(session)
        
    print(f"{'exercice: {}'.format(session['name_exercise']):-^60}")
    
    print(session)
    session['error'] = ''
    print()
    print(f"{' '*14}Trouver: {session['question']['note']} + {session['question']['demi_ton']} demi tons".ljust(20))
    print(session['question']['answer'])
    
    
def find_note_negatif(session):
    pass
    
def find_demi_ton_positif(session):
    pass
    
def find_demi_ton_negatif(session):
    pass
    
    
def init_question(session):
    session['start'] = time.time()
    session['name_exercise'] = inspect.stack()[0][3]
    question = new_question()
    question["count"] = 1
    session['question'] = question
    return session

def next_question(session):
    question = new_question()
    question["count"] = session['question']['count'] + 1
    session['question'] = question
    return session

def new_question():
    note = choice(NOTES)
    demi_ton = choice(list(range(1,12)))
    index_note = NOTES.index(note)
    new_index = (index_note + demi_ton) % 12
    
    return {
        "note": note,
        "demi_ton": demi_ton,
        "answer": NOTES[new_index],
    }