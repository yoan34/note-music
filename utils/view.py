import os
import time

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
    session['name_exercise'] = __name__
    print(session['name_exercise'])
    print(f"{'exercice: {}'.format(__name__):-^60}")
    
    
def find_note_negatif(session):
    pass
    
def find_demi_ton_positif(session):
    pass
    
def find_demi_ton_negatif(session):
    pass
    
    