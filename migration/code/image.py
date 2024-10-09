import json
from dotenv import load_dotenv
import os
import io
import requests

load_dotenv()

def update_character_image():
    character_json: list = json.load(open('result/data/character.json', 'r', encoding='utf-8'))
    base_url = f'{os.getenv("ORACLE_UPLOAD_URL")}/o/aecheck/'

    for character in character_json:
        id = int(character["id"])

        for suffix in ['.webp', '.png']:
            original_name = f'result/image/{id}{suffix}'
            with open(original_name, 'rb') as f:
                img_bytes = io.BytesIO(f.read())
            new_name = f'character/char{str(id).zfill(4)}{suffix}'

            requests.put(f'{base_url}{new_name}', data=img_bytes)
        
        if "staralign.true" in character["tags"]:
            for suffix in ['.webp', '.png']:
                original_name = f'result/image/{id}_awaken{suffix}'
                with open(original_name, 'rb') as f:
                    img_bytes = io.BytesIO(f.read())
                new_name = f'staralign/char{str(id).zfill(4)}{suffix}'

                requests.put(f'{base_url}{new_name}', data=img_bytes)
        print('.', end='', flush=True)

def update_buddy_image():
    buddy_json: list = json.load(open('result/data/buddy.json', 'r', encoding='utf-8'))
    base_url = f'{os.getenv("ORACLE_UPLOAD_URL")}/o/aecheck/'

    for buddy in buddy_json:
        id = int(buddy["id"])

        for suffix in ['.webp', '.png']:
            original_name = f'result/image/{id}{suffix}'
            with open(original_name, 'rb') as f:
                img_bytes = io.BytesIO(f.read())
            new_name = f'buddy/buddy{str(id).zfill(4)}{suffix}'

            requests.put(f'{base_url}{new_name}', data=img_bytes)

        print('!', end='', flush=True)


if __name__ == '__main__':
    update_character_image()
    update_buddy_image()