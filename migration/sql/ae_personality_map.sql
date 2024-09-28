CREATE TABLE personality_mappings (
    id              SERIAL PRIMARY KEY,
    character_id    VARCHAR(20) NOT NULL,
    personality_id  VARCHAR(20) NOT NULL,
    description     VARCHAR(500),
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP,
    deleted_at      TIMESTAMP
);