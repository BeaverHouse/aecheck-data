import openpyxl
import bs4
import urllib.parse
from urllib.request import urlopen
from config import (
    STAR4_TITLE,
    STAR5_TITLE, 
    SEESAA_URL,
    FILE_NAME,
    PERSONALITY_SHEET_NAME
)
from function import clean_sheet
import datetime

def get_seesaa_url(word: str) -> str:
    enc_word = urllib.parse.quote(word, encoding='euc-jp')
    return "{}/d/{}".format(SEESAA_URL, enc_word)


def get_bs(url: str) -> bs4.BeautifulSoup:
    html = urlopen(url)
    return bs4.BeautifulSoup(html, "lxml", from_encoding='utf-8')


def parse_bs(object: bs4.BeautifulSoup, write_year: bool = False) -> None:
    today = datetime.date.today()

    table = object.find("table", { "id": "content_block_5" })
    
    # no typesafe
    table_rows = table.find_all("tr")

    dic = {}
    for row in table_rows[1:]:
        cells = row.find_all("td")

        name:               str = cells[0].text.replace("?", "")
        elements:           str = cells[1].text
        personalities:      str = cells[6].text
        year:               str = cells[7].text.split("(")[0]
        
        # 테일즈 시온 동명이인 처리
        if name == "シオン" and year == "2022":
            name = "シオン (テイルズ)"
        # 이시층 처리
        if "異時層" in name:
            name = name.split("(")[0]
        
        new_personalities = personalities.replace(" ", "").split(",")
        for element in elements:
            # 짚돌이 속성표기 예외처리
            if element != "※":
                new_personalities.append(element)

        dic[name] = {
            "personalities": new_personalities,
            "year": year if write_year else None
        }

    wb = openpyxl.open(FILE_NAME, data_only=True)
    
    if PERSONALITY_SHEET_NAME not in wb:
        print("create sheet")
        wb.create_sheet(PERSONALITY_SHEET_NAME)
        sheet = wb[PERSONALITY_SHEET_NAME]
        sheet.append(["일어 이름", "특성", "출시년도", "업데이트"])
    else:
        sheet = wb[PERSONALITY_SHEET_NAME]
    
    # 시트의 첫 열 = key값 = 일어 이름
    key_list = list(filter(lambda x: x is not None and len(x) > 0, [i[0].value for i in sheet.iter_rows(min_row=2)]))

    exclude_name = ["アルド", "リュゼ", "サザンカ", "フラムラピス", "フラムラピス(AS)", "ディアドラ", "アルテナ", "フィーネ"]
    for n, p in dic.items():
        personality_str = ",".join(p["personalities"])
        year = p["year"]

        if n not in key_list:
            print("add", n)
            sheet.append([n, personality_str, year, today])
        else:
            if n in exclude_name: continue
            row_idx = key_list.index(n) + 1
            target_row = list(sheet.rows)[row_idx]
            if target_row[1].value != personality_str:
                print(f"update {n} : {target_row[1].value} -> {personality_str}")
                target_row[1].value = personality_str
                target_row[3].value = today

    clean_sheet(sheet)
    wb.save(FILE_NAME)



# execute
if __name__ == "__main__":
    
    five_url = get_seesaa_url(STAR5_TITLE)
    five_bs = get_bs(five_url)
    parse_bs(five_bs, write_year=True)

    four_url = get_seesaa_url(STAR4_TITLE)
    four_bs = get_bs(four_url)
    parse_bs(four_bs)