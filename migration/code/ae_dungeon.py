import json
import datetime
from psycopg2.extras import execute_values

from postgres import get_postgres

TABLE_NAME = "aecheck.dungeons"

def update_ae_dungeon():    
    time = datetime.datetime.now()
    dungeon_json: list = json.load(open('result/data/dungeon.json', 'r', encoding='utf-8'))

    dungeon_data = list(map(
        lambda x: [
            "dungeon" + str(x['id']).zfill(4), 
            x['altema'],
            x['wiki'],
        ],
        dungeon_json
    ))

    with get_postgres() as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT dungeon_id FROM {TABLE_NAME}")
        current_ids = list(map(lambda x: x[0], cur.fetchall()))
            
        update_info = [x for x in dungeon_data if x[0] not in current_ids]

        if not update_info:
            print("nothing to update")
            return
        execute_values(
            cur,
            f"INSERT INTO {TABLE_NAME} (dungeon_id, altema_url, aewiki_url) VALUES %s",
            update_info
        )
        conn.commit()

if __name__ == "__main__":
    update_ae_dungeon()


