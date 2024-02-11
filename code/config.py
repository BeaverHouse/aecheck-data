# Seesaa Wiki base URL
SEESAA_URL = "https://anothereden.game-info.wiki"

STAR4_TITLE = "☆4キャラ一覧"
STAR5_TITLE = "☆5キャラ一覧"
BUDDY_TITLE = "バディ一覧"


# 데이터 관련 - 변경되면 수정해 주세요
FILE_NAME = "data.xlsx"
IMG_SOURCE_PATH = "rawimage"

CHARACTER_SHEET_NAME =      "캐릭터"
BUDDY_SHEET_NAME =          "버디"
PERSONALITY_SHEET_NAME =    "v3_seesaa"
DUNGEON_SHEET_NAME =        "dungeon"
TRANSLATE_SHEET_NAME =      "v3_translate"


# 결과 관련 - 변경되면 수정해 주세요
RESULT_PATH = "result"

PARSE_REF_DICT = {
    "style": {
        "4.5" :     "style.four",
        "NS" :      "style.normal",
        "AS" :      "style.another",
        "ES" :      "style.extra", 
    },
    "get": {
        "FALSE":    "get.notfree",
        "TRUE":     "get.free",
    },
    "type": {
        "천":       "type.light",
        "명":       "type.shadow",
    },
    "alter": {
        "FALSE":    "alter.false",
        "TRUE":     "alter.true",
    },
    "staralign": {
        "FALSE":    "staralign.false",
        "TRUE":     "staralign.true",
    },
    "manifest": {
        "없음":         "manifest.step0",
        "현현":         "manifest.step1",
        "진현현":       "manifest.step2",
    },
    "img_parse": {
        "4.5": "",
        "NS": "_rank5",
        "AS": "_s2_rank5",
        "ES": "_s3_rank5"
    }
}

AC_MAPPING = {
    "碧光の鎌使い": "Suzette_(Alter)",
    "紫装の槍使い": "Toova_(Alter)",
    "銀織の雷使い": "Premaya_(Alter)",
    "赤套の炎使い": "Dewey_(Alter)",
    "黒衣の刀使い": "Isuka_(Alter)",
}