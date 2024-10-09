CREATE TABLE dungeons (
    dungeon_id          VARCHAR(20) NOT NULL,
    altema_url          VARCHAR(500),
    aewiki_url          VARCHAR(500),
    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP,
    deleted_at          TIMESTAMP,
    CONSTRAINT ae_dungeon_pk PRIMARY KEY (dungeon_id)
);