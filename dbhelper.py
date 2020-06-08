import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

db = sqlite3.connect(DB_PATH)
cursor = db.cursor()


cursor.execute('create table if not exists like ('
               'id integer primary key autoincrement, '
               'user_id string, '
               'animal string(10), '
               'name string(50))')


def get_name(animal, sex=None):
    sex_cond = f"where sex = '{sex}'" if sex else ''
    return cursor.execute(f"select name, sex from {animal} {sex_cond} order by random() limit 1").fetchone()[0]


def add_wtf(res, req, session):
    with open(os.path.join(BASE_DIR, 'wtf.txt'), 'a', encoding='utf8') as file:
        file.write(f'{session["state"]}: {req.text}\n')


def put_like(user_id, animal, name):
    cursor.execute('insert into like(user_id, animal, name) values(?, ?, ?)',
                   (user_id, animal, name))
    db.commit()


def get_likes(user_id):
    return cursor.execute(f"select name, animal from like where user_id = '{user_id}'").fetchall()


if __name__ == '__main__':
    while True:
        cursor.execute(input())
        [print(i) for i in cursor.fetchall()]
        db.commit()