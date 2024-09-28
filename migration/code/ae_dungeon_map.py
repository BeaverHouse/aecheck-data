import json
import datetime
from psycopg2.extras import execute_values

from postgres import get_postgres

TABLE_NAME = "aecheck.ae_dungeon_map"

def update_ae_dungeon_map():    
    time = datetime.datetime.now()
    character_json: list = json.load(open('result/data/character.json', 'r', encoding='utf-8'))
    
    update_info = []
    for character in character_json:
        dungeons = [f'dungeon{str(x).zfill(4)}' for x in character["dungeon_drop"]] if "dungeon_drop" in character else []
        for dungeon in dungeons:
            update_info.append([
                f'char{str(character["id"]).zfill(4)}',
                dungeon
            ])

    with get_postgres() as conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {TABLE_NAME} WHERE character_id LIKE 'char%'")
            
        execute_values(
            cur,
            f"""INSERT INTO {TABLE_NAME} (
                character_id,
                dungeon_id
            ) VALUES %s""",
            update_info
        )
        conn.commit()

if __name__ == "__main__":
    update_ae_dungeon_map()


