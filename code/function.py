import json
import os
import shutil
from openpyxl.worksheet.worksheet import Worksheet

def write_json(path: str, json_data):
    """json 값을 해당 경로에 파일로 저장하는 함수"""
    with open(path, 'w+', encoding='utf-8') as f:
        json.dump(json_data, f, indent="\t", ensure_ascii=False)


def init_folder(path: str):
    """폴더 초기화 + 생성"""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def clean_sheet(sheet: Worksheet):
    """시트의 첫 칸이 비어 있는 행을 정리하는 함수"""
    for idx, row in enumerate(sheet.iter_rows()):
        val = row[0].value
        if val is None or len(val) <= 0:
            sheet.delete_rows(idx + 1)