import json
import datetime
from psycopg2.extras import execute_values

from postgres import get_postgres

TABLE_NAME = "aecheck.ae_i18n"

buddy_json: list = json.load(open('result/data/buddy.json', 'r', encoding='utf-8'))

def parse_key(key: str):
    if key.startswith("book.char"):
        num = key.replace("book.char", "")
        return "book.char" + str(num).zfill(4)
    elif key.startswith("bud"):
        code = key.replace("bud", "")
        buddy = list(filter(lambda x: str(x['code']) == code, buddy_json))[0]
        return "buddy" + str(buddy['id'])
    elif key.startswith("drop.dungeon"):
        num = key.replace("drop.dungeon", "")
        return "dungeon" + str(num).zfill(4)
    elif key.startswith("personality.p"):
        return "personality" + key.replace("personality.p", "")
    return key

def update_ae_i18n():    
    time = datetime.datetime.now()
    ko_json: list = json.load(open('result/i18n/ko.json', 'r', encoding='utf-8'))
    ja_json: list = json.load(open('result/i18n/jp.json', 'r', encoding='utf-8'))
    en_json: list = json.load(open('result/i18n/en.json', 'r', encoding='utf-8'))

    i18n_data = list(map(
        lambda x: [
            parse_key(x),
            ko_json[x],
            en_json[x],
            ja_json[x],
        ],
        ko_json.keys()
    ))

    with get_postgres() as conn:
        cur = conn.cursor()

        cur.execute(f"DELETE FROM {TABLE_NAME}")

        execute_values(
            cur,
            f"INSERT INTO {TABLE_NAME} (key, ko, en, ja) VALUES %s",
            i18n_data
        )

        conn.commit()

if __name__ == "__main__":
    update_ae_i18n()


