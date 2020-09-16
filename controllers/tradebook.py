# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from tradebook.py")

def view():
    #Displays Table Tradebook, if empty goes to insert_table
    rows = db(db.tradebook).select() or db.tradebook.import_from_csv_file(open('C:/Users/HP/OneDrive/Desktop/UBS Training/web2py/web2py/applications/watchDogs/Sample Data/tradebook.csv', 'r', encoding='utf-8', newline=''))
    rows = db(db.tradebook).select()
    return locals()
