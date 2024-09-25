import json

from oracle import get_oracle

TABLE_NAME = "ae_buddy"

def update_ae_buddy():    
    buddy_json: list = json.load(open('result/data/buddy.json', 'r', encoding='utf-8'))

    buddy_data = list(map(
        lambda x: [
            "buddy" + str(x['id']), 
            "char" + str(x['link'][0]) if x['link'] else None,
            x['get'],
            x['seesaa'],
            x['aewiki']
        ],
        buddy_json
    ))

    with get_oracle() as conn:
        cur = conn.cursor()
        current_ids = list(map(lambda x: x[0], cur.execute(f"SELECT buddy_id FROM {TABLE_NAME}").fetchall()))
            
        update_info = [x for x in buddy_data if x[0] not in current_ids]
        if not update_info:
            print("nothing to update")
            return
        cur.executemany(
            f"INSERT INTO {TABLE_NAME} (buddy_id, character_id, get_path, seesaa_url, aewiki_url) VALUES (:1, :2, :3, :4, :5)",
            update_info
        )
        conn.commit()

if __name__ == "__main__":
    update_ae_buddy()


