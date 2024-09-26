import json
import datetime

from oracle import get_oracle

TABLE_NAME = "ae_personality_map"

def update_ae_personality_map():    
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    character_json: list = json.load(open('result/data/character.json', 'r', encoding='utf-8'))
    
    update_info = []
    for character in character_json:
        personalities = [x for x in character["tags"] if "personality" in x]
        for personality in personalities:
            update_info.append([
                f'char{character["id"]}',
                f'personality{personality.replace("personality.p", "")}',
                time
            ])

    with get_oracle() as conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {TABLE_NAME} WHERE character_id LIKE 'char%'")
            
        cur.executemany(
            f"""INSERT INTO {TABLE_NAME} (
                character_id,
                personality_id,
                created_at
            ) VALUES (
                :1, :2, :3
            )""",
            update_info
        )
        conn.commit()

if __name__ == "__main__":
    update_ae_personality_map()


