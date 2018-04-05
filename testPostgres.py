from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


connect_str = "dbname='testpython' user='mat' host='localhost' " + \
                  "password='manamsirajdi12'"
conn = psycopg2.connect(connect_str)
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE library (
# id SERIAL PRIMARY KEY,
# name VARCHAR NOT NULL,
# author VARCHAR NOT NULL,
# genre VARCHAR NOT NULL,
# language VARCHAR NOT NULL
# );""")
print('')
print('Welcome to the Library! Select your action by the following triggers:')
print('')
def main():
    print('# - Input new book into library === INPUT')
    print('# - Search a book from library  === SEARCH')
    print('# - Delete a book from library  === DELETE')

    command = input()
    if command.lower() == 'exit':
        exit()
    if command.lower() == 'input':
        print('Write name: ', end='')
        nam = input()
        print('Write author: ', end='')
        auth = input()
        print('Write genre: ', end='')
        gen = input()
        print('Write language: ', end='')
        lang = input()

        cursor.execute("""INSERT INTO library
        (name, author, genre, language)
        VALUES (%s, %s, %s, %s)""", (nam, auth, gen, lang));
        conn.commit()

    if command.lower() == 'search':
        print('What is your trigger?')
        print('###-NAME')
        print('###-AUTHOR')
        print('###-GENRE')
        print('###-LANGUAGE')
        print('')
        print('###-', end='')
        trigger = input()
        print('OK! Write a word: ', end='')

        if trigger.lower() == 'name':
            word = input()
            cursor.execute("SELECT * FROM library WHERE name = (%s)", (word,));
            rows = cursor.fetchall()
            for col in rows:
                print(col)
        elif trigger.lower() == 'author':
            word = input()
            cursor.execute("SELECT * FROM library WHERE name = (%s)", (word,));
            rows = cursor.fetchall()
            for col in rows:
                print(col)
        elif trigger.lower() == 'genre':
            word = input()
            cursor.execute("SELECT * FROM library WHERE name = (%s)", (word,));
            rows = cursor.fetchall()
            for col in rows:
                print(col)
        elif trigger.lower() == 'language':
            word = input()
            cursor.execute("SELECT * FROM library WHERE name = (%s)", (word,));
            rows = cursor.fetchall()
            for col in rows:
                print(col)

    cursor.execute("""SELECT * FROM library;""")
    rows = cursor.fetchall()
    print(rows)

if __name__ == '__main__':
    while True:
        main()
