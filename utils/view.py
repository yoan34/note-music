def showView(path, session):
    dispatcher = {
        'home': home,
        'find_note_positif': findNotePositif,
        'find_note_negatif': findNoteNegatif,
        'find_demi_ton_positif': findDemiTonPositif,
        'find_demi_ton_negatif': findNoteNegatif,
    }
    dispatcher[path](session)
        
def home(session):
    print(f"{'exercice guitar':-^60}")
    print('')
    print(f"{'1 - find note positif':>40}")
    print(f"{'2 - find note negatif':>40}")
    print(f"{'3 - find demi-ton positif':>44}")
    print(f"{'4 - find demi-ton positif':>44}")
    print()
    print("-"*60)
        
    
def findNotePositif(session):
    pass
    
def findNoteNegatif(session):
    pass
    
def findDemiTonPositif(session):
    pass
    
def findDemiTonNegatif(session):
    pass
    
    