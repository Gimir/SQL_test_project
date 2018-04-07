from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)


connect_str = "dbname='testpython' user='mat' host='localhost' " + \
                  "password='manamsirajdi12'"
conn = psycopg2.connect(connect_str)
cursor = conn.cursor()

def checkSize(arr):
    lengthOfTable = len(arr[0])
    tableOfLength = []

    for j in range(lengthOfTable):
        maxlength2 = 0
        for i in arr:
            if type(i[j]) is not int:
                maxlength1 = len(i[j])
            else:
                maxlength1 = len(str(i[j]))
            if maxlength1 > maxlength2:
                maxlength2 = maxlength1
        tableOfLength.append(maxlength2)
    return tableOfLength

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
    print('')
    print('###- Input the new book into library === INPUT')
    print('###- Search the book from library    === SEARCH')
    print('###- Delete the book from library    === DELETE')
    print('###- Change something from library   === CHANGE')
    print('###- Display the table               === DISPLAY')
    print('')
    print('###- ', end='')

    command = input()
    if command.lower() == 'exit':
        exit()
    if command.lower() == 'input':
        os.system('clear')
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
        os.system('clear')
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

    if command.lower() == 'delete':
        os.system('clear')
        print('What you want to delete? Type name of the book: ', end='')
        word = input()
        cursor.execute("DELETE FROM library WHERE name = (%s)", (word,))
        conn.commit()

    if command.lower() == 'change':
        os.system('clear')
        print('Type name of book: ', end='')
        word = input()
        print('')
        print('What you want to change?')
        print('###- NAME')
        print('###- AUTHOR')
        print('###- GENRE')
        print('###- LANGUAGE')
        print('')
        print('###- ', end='')
        trigger = input()
        print('')
        print('###- Type your change here: ', end='')
        change = input()
        print('')

        if trigger.lower() == 'name':
            cursor.execute("UPDATE library SET name = %s WHERE name = (%s)", (change, word,));
            conn.commit()
        elif trigger.lower() == 'author':
            cursor.execute("UPDATE library SET author = %s WHERE name = (%s)", (change, word,));
            conn.commit()
        elif trigger.lower() == 'genre':
            cursor.execute("UPDATE library SET genre = %s WHERE name = (%s)", (change, word,));
            conn.commit()
        elif trigger.lower() == 'language':
            cursor.execute("UPDATE library SET language = %s WHERE name = (%s)", (change, word,));
            conn.commit()


    if command.lower() == 'display':
        os.system('clear')
        cursor.execute("SELECT * FROM library");
        rows = cursor.fetchall()
        a = checkSize(rows)
        for cup in rows:
            ind = 0
            for word in cup:
                print(' {} '.format(word), end='')

                for i in range(a[ind] - len(str(word))):
                    print(' ', end='')
                print('|', end='')
                ind = ind + 1
            print('')



if __name__ == '__main__':
    while True:
        print('')
        main()
