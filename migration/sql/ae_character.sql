CREATE TABLE ae_character (
    character_id            VARCHAR(20) NOT NULL,
    character_code          VARCHAR(20) NOT NULL,
    category                VARCHAR(20) NOT NULL,
    style                   VARCHAR(10) NOT NULL,
    light_shadow            VARCHAR(10) NOT NULL,
    max_manifest            INTEGER NOT NULL,
    is_awaken               INTEGER NOT NULL,
    is_alter                INTEGER NOT NULL,
    alter_character         VARCHAR(20),
    seesaa_url              VARCHAR(500),
    aewiki_url              VARCHAR(500),
    update_date             DATE,
    created_at              TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at              TIMESTAMP,
    deleted_at              TIMESTAMP,
    CONSTRAINT ae_character_pk PRIMARY KEY (character_id)
);