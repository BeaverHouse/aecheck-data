CREATE TABLE ae_personality_map (
    id              NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    character_id    VARCHAR2(20) NOT NULL,
    personality_id  VARCHAR2(20) NOT NULL,
    description     VARCHAR2(500),
    created_at      TIMESTAMP(6) NOT NULL,
    updated_at      TIMESTAMP(6),
    deleted_at      TIMESTAMP(6)
);