import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

db = sqlite3.connect(DB_PATH)
cursor = db.cursor()


def get_name(animal, sex=None):
    sex_cond = f"where sex = '{sex}'" if sex else ''
    return cursor.execute(f"select name, sex from {animal} {sex_cond} order by random() limit 1").fetchone()[0]
