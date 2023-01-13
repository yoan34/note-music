NOTES = ["do", "do#", "re", "re#", "mi", "fa", "fa#",
         "sol", "sol#", "la", "la#", "si"]

def analyseInputUser(session):
    path = session['path']
    choice = session['user']
    
    if path != 'home' and choice.upper() == 'B':
        session['path'] = 'home'
        return session
    
    if path == 'home':
        if choice == '1':
            session['path'] = 'find_note_positif'
        if choice == '2':
            session['path'] = 'find_note_negatif'
        if choice == '3':
            session['path'] = 'find_demi_ton_positif'
        if choice == '4':
            session['path'] = 'find_demi_ton_negatif'
            
    
    return session