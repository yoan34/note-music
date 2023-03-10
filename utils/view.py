import os
import time
import datetime
from random import choice
from utils.tools import NOTES, NB_QUESTION

clear = lambda: os.system('clear')

def showView(session):
    dispatcher = {
        'home': home,
        'find_note_positif': find_note_positif,
        'find_note_negatif': find_note_negatif,
        'find_demi_ton_positif': find_demi_ton_positif,
        'find_demi_ton_negatif': find_demi_ton_negatif,
        'end_session': end_session,
    }
    clear()
    dispatcher[session['path']](session)
        
def home(session):
    print(session)
    print(f"{'exercice guitar':-^60}")
    print('')
    print(f"{'1 - find note positif':>40}")
    print(f"{'2 - find note negatif':>40}")
    print(f"{'3 - find demi-ton positif':>44}")
    print(f"{'4 - find demi-ton positif':>44}")
    print()
    print("-"*60)

def end_session(session):
    print(session)
    print(f"{'exercice: {} [END] '.format(session['name_exercise']):-^60}")
    print()
    if session['question'] is not None:
        session['end'] = time.time()

        result = f"{session['good_answer']}/{session['question']['count']}"
        result += f"  {(session['good_answer']/session['question']['count']*100):.2f}%"
        result += f"  {(session['end'] - session['start'])/session['question']['count']:.2f}s"
        result += f"  {datetime.datetime.now().strftime('%d/%m/%Y')}"
        print(result)
        print()
        print('-'*60)
        print(f"data/{session['name_exercise']}.txt")
        f = open(f"data/{session['name_exercise']}.txt", "a")
        f.write(result+"\n")
        f.close()
        session['error'] = 'start'
        session['n_error'] = 0
        session['question'] = None
        session['good_answer'] = 0
    else:
        print('Back to home [b]')
        
    
def find_note_positif(session):
    if session['question'] is None:
        session = next_question(session, first=True)
    if not session['error'] or session['n_error'] == 3:
        session = next_question(session)
        session['n_error'] = 0
    if session['question']['count'] == NB_QUESTION:
        session['path'] = 'end_session'
        return
        
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
    

def next_question(session, first=False):
    if first:
        session['start'] = time.time()
        session['name_exercise'] = session['path']
        question = new_question()
        question["count"] = 1
    else:
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