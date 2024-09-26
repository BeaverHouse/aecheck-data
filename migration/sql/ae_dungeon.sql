CREATE TABLE ae_dungeon (
    dungeon_id          VARCHAR2(10) NOT NULL,
    altema_url          VARCHAR2(500),
    aewiki_url          VARCHAR2(500),
    CONSTRAINT ae_dungeon_pk PRIMARY KEY (dungeon_id)
);