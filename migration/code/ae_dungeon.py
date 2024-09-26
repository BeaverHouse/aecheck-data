import json
import datetime

from oracle import get_oracle

TABLE_NAME = "ae_dungeon"

def update_ae_dungeon():    
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dungeon_json: list = json.load(open('result/data/dungeon.json', 'r', encoding='utf-8'))

    dungeon_data = list(map(
        lambda x: [
            "dungeon" + str(x['id']), 
            x['altema'],
            x['wiki'],
            time
        ],
        dungeon_json
    ))

    with get_oracle() as conn:
        cur = conn.cursor()
        current_ids = list(map(lambda x: x[0], cur.execute(f"SELECT dungeon_id FROM {TABLE_NAME}").fetchall()))
            
        update_info = [x for x in dungeon_data if x[0] not in current_ids]

        if not update_info:
            print("nothing to update")
            return
        cur.executemany(
            f"INSERT INTO {TABLE_NAME} (dungeon_id, altema_url, aewiki_url, created_at) VALUES (:1, :2, :3, :4)",
            update_info
        )
        conn.commit()

if __name__ == "__main__":
    update_ae_dungeon()


