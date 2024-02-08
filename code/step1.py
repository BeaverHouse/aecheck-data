import openpyxl
from openpyxl.workbook.workbook import Workbook
from config import (
    FILE_NAME,
    CHARACTER_SHEET_NAME,
    BUDDY_SHEET_NAME,
    PERSONALITY_SHEET_NAME,
    DUNGEON_SHEET_NAME,
    TRANSLATE_SHEET_NAME,
)
import sys



def add_personality_tags(wb: Workbook) -> None:
    if PERSONALITY_SHEET_NAME not in wb or TRANSLATE_SHEET_NAME not in wb:
        print("참조할 시트가 없습니다.")
        sys.exit()
    
    p_sheet = wb[PERSONALITY_SHEET_NAME]
    t_sheet = wb[TRANSLATE_SHEET_NAME]

    # 일어 퍼스널리티 리스트 작성
    p_list: list[str] = []
    for row in p_sheet.iter_rows(min_row=2):
        p_list += row[1].value.split(",")
    p_list = list(set(p_list))


    # 번역시트의 3열 = 일어 
    key_list = list(filter(lambda x: x is not None and len(x) > 0, [i[2].value for i in t_sheet.iter_rows(min_row=2)]))
    for p in p_list:
        if p not in key_list:
            print("add personality", p)
            t_sheet.append(["", "", p])


def add_char_book_tags(wb: Workbook) -> None:
    if CHARACTER_SHEET_NAME not in wb or TRANSLATE_SHEET_NAME not in wb:
        print("참조할 시트가 없습니다.")
        sys.exit()
    
    c_sheet = wb[CHARACTER_SHEET_NAME]
    t_sheet = wb[TRANSLATE_SHEET_NAME]

    # 한국어명 dic 작성
    name_dic = {}
    book_dic = {}
    for row in c_sheet.iter_rows(min_row=2):
        id = row[0].value
        name = row[1].value
        code = row[3].value
        book = row[12].value
    
        name_dic[code] = name
        if book is not None and len(book) > 0:
            book_dic[id] = book


    # 번역시트의 1열 = 태그
    key_list = list(filter(lambda x: x is not None and len(x) > 0, [i[0].value for i in t_sheet.iter_rows(min_row=2)]))
    for code in name_dic:
        tag = "c{}".format(code)
        if tag not in key_list:
            print("add tag", tag)
            kor_name = name_dic[code]
            t_sheet.append([tag, kor_name])
    for id in book_dic:
        tag = "book.char{}".format(id)
        if tag not in key_list:
            print("add tag", tag)
            kor_name = book_dic[id]
            t_sheet.append([tag, kor_name])


def add_buddy_tags(wb: Workbook) -> None:
    if BUDDY_SHEET_NAME not in wb or TRANSLATE_SHEET_NAME not in wb:
        print("참조할 시트가 없습니다.")
        sys.exit()
    
    b_sheet = wb[BUDDY_SHEET_NAME]
    t_sheet = wb[TRANSLATE_SHEET_NAME]

    buddy_dic = {}
    for row in b_sheet.iter_rows(min_row=2):
        name = row[1].value
        code = row[2].value
    
        buddy_dic[code] = name

    # 번역시트의 1열 = 태그 
    key_list = list(filter(lambda x: x is not None and len(x) > 0, [i[0].value for i in t_sheet.iter_rows(min_row=2)]))
    for code in buddy_dic:
        tag = "bud{}".format(code)
        if tag not in key_list:
            print("add tag", tag)
            kor_name = buddy_dic[code]
            t_sheet.append([tag, kor_name])



def add_dungeon_tags(wb: Workbook) -> None:
    if DUNGEON_SHEET_NAME not in wb or TRANSLATE_SHEET_NAME not in wb:
        print("참조할 시트가 없습니다.")
        sys.exit()
    
    d_sheet = wb[DUNGEON_SHEET_NAME]
    t_sheet = wb[TRANSLATE_SHEET_NAME]

    # 한국어명 dic 작성
    dungeon_dic = {}
    for row in d_sheet.iter_rows(min_row=2):
        id = row[0].value
        name = row[1].value
    
        dungeon_dic[id] = name
 
    # 시트의 1열 = key값 = 태그 
    key_list = list(filter(lambda x: x is not None and len(x) > 0, [i[0].value for i in t_sheet.iter_rows(min_row=2)]))
    for id in dungeon_dic:
        id_str = str(id).zfill(3)
        tag = "drop.dungeon{}".format(id_str)
        if tag not in key_list:
            print("add tag", tag)
            kor_name = dungeon_dic[id]
            t_sheet.append([tag, kor_name])

def make_translate_sheet() -> None:
    wb = openpyxl.open(FILE_NAME, data_only=True)
    
    add_personality_tags(wb=wb)
    add_char_book_tags(wb=wb)
    add_buddy_tags(wb=wb)
    add_dungeon_tags(wb=wb)

    wb.save(FILE_NAME)



# execute
if __name__ == "__main__":    
    make_translate_sheet()