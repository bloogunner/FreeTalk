import sqlite3 

connection = sqlite3.connect("translations.db")

cursor = connection.cursor()

'''Create the table if it doesn't already exist.'''
cursor.execute(
    '''
    Create table If not exists translations (
        id integer primary key autoincrement,
        source_language text not null,
        target_language text not null,
        original_text text not null,
        translated_text text not null
    )
    '''
)

# insert a translation.

cursor.execute(""" 
               INSERT INTO translations (
                   source_language,
                   target_language,
                   original_text,
                   translated_text
                   
               )
               VALUES(?,?,?,?)
           """, ("en",
                 "es",
                 "Hello",
                 "Hola"
                 ))


# Persist the changes.
connection.commit()

connection.close()