import json
import datetime
from psycopg2.extras import execute_values

from postgres import get_postgres

TABLE_NAME = "aecheck.buddies"

def update_ae_buddy():    
    time = datetime.datetime.now()
    buddy_json: list = json.load(open('result/data/buddy.json', 'r', encoding='utf-8'))

    buddy_data = list(map(
        lambda x: [
            "buddy" + str(x['id']), 
            "char" + str(x['link'][0]).zfill(4) if x['link'] else None,
            x['get'] if x['get'] and x['get'].strip() != "get.notfree" else None,
            x['seesaa'],
            x['aewiki']
        ],
        buddy_json
    ))

    with get_postgres() as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT buddy_id FROM {TABLE_NAME}")
        current_ids = list(map(lambda x: x[0], cur.fetchall()))
            
        update_info = [x for x in buddy_data if x[0] not in current_ids]
        if not update_info:
            print("nothing to update")
            return
        execute_values(
            cur,
            f"INSERT INTO {TABLE_NAME} (buddy_id, character_id, get_path, seesaa_url, aewiki_url) VALUES %s",
            update_info
        )
        conn.commit()

if __name__ == "__main__":
    update_ae_buddy()


