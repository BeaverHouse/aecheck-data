CREATE TABLE ae_dungeon (
    dungeon_id          VARCHAR2(20) NOT NULL,
    altema_url          VARCHAR2(500),
    aewiki_url          VARCHAR2(500),
    created_at          TIMESTAMP(6) NOT NULL,
    updated_at          TIMESTAMP(6),
    deleted_at          TIMESTAMP(6),
    CONSTRAINT ae_dungeon_pk PRIMARY KEY (dungeon_id)
);