CREATE TABLE ae_dungeon (
    id              NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    character_id    VARCHAR2(20) NOT NULL,
    personality_id  VARCHAR2(20) NOT NULL,
    description     VARCHAR2(500) NOT NULL,
    created_at      TIMESTAMP(6) NOT NULL,
    updated_at      TIMESTAMP(6),
    deleted_at      TIMESTAMP(6)
);