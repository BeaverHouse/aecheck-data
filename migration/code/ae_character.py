import json
import datetime

from oracle import get_oracle

TABLE_NAME = "ae_character"

def get_category(character) -> str:
    colab_personalities = [
        "personality.p053", # 페르소나
        "personality.p054", # 크로노 크로스
        "personality.p068", # 테일즈
        "personality.p107", # KOF
        "personality.p105", # 옥토패스
    ]
    if any(x in colab_personalities for x in character["tags"]): return "COLAB"
    elif "get.free" in character["tags"]: return "FREE"
    else: return "ENCOUNTER"

def get_style(character) -> str:
    if "style.extra" in character["tags"]: return "ES"
    elif "style.another" in character["tags"]: return "AS"
    elif "style.normal" in character["tags"]: return "NS"
    else: return "4☆"

def get_manifest_level(character) -> int:
    manifest_tags = list(filter(lambda x: "manifest" in x, character["tags"]))
    if len(manifest_tags) == 0: return 0
    else: return int(manifest_tags[0].replace("manifest.step", ""))

def get_alter_character(character, character_json) -> str:
    if "change" not in character: return None
    for id in character["change"]:
        target = list(filter(lambda x: x["id"] == id, character_json))[0]
        if target["code"] != character["code"]:
            return target["code"]
    return None

def update_ae_dungeon():    
    time = datetime.datetime.now()
    character_json: list = json.load(open('result/data/character.json', 'r', encoding='utf-8'))
    
    character_data = list(map(
        lambda x: [
            f'char{str(x["id"]).zfill(4)}', 
            f'c{x['code']}',
            get_category(x),
            get_style(x),
            "light" if "type.light" in x["tags"] else "dark",
            get_manifest_level(x),
            1 if "staralign.true" in x["tags"] else 0,
            1 if "alter.true" in x["tags"] else 0,
            f'c{get_alter_character(x, character_json)}' if get_alter_character(x, character_json) else None,
            x["seesaa"] if "seesaa" in x else None,
            x["aewiki"] if "aewiki" in x else None,
            datetime.datetime.strptime(x["year"], "%Y/%m/%d") if "year" in x else None,
            time
        ],
        character_json
    ))

    with get_oracle() as conn:
        cur = conn.cursor()
        current_ids = list(map(lambda x: x[0], cur.execute(f"SELECT character_id FROM {TABLE_NAME}").fetchall()))
            
        update_info = [x for x in character_data if x[0] not in current_ids]
        if not update_info:
            print("nothing to update")
            return
        cur.executemany(
            f"""INSERT INTO {TABLE_NAME} (
                character_id,
                character_code,
                category,
                style,
                light_shadow,
                max_manifest,
                is_awaken,
                is_alter,
                alter_character,
                seesaa_url,
                aewiki_url,
                update_date,
                created_at
            ) VALUES (
                :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13
            )""",
            update_info
        )
        conn.commit()

if __name__ == "__main__":
    update_ae_dungeon()


