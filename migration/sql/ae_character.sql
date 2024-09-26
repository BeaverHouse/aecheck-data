CREATE TABLE ae_character (
    character_id            VARCHAR2(20) NOT NULL,
    character_code          VARCHAR2(20) NOT NULL,
    category                VARCHAR2(20) NOT NULL,
    style                   VARCHAR2(10) NOT NULL,
    light_shadow            VARCHAR2(10) NOT NULL,
    max_manifest            NUMBER(3) NOT NULL,
    is_awaken               NUMBER(1) NOT NULL,
    is_alter                NUMBER(1) NOT NULL,
    alter_character         VARCHAR2(20),
    seesaa_url              VARCHAR2(500),
    aewiki_url              VARCHAR2(500),
    update_date             DATE,
    created_at              TIMESTAMP(6) NOT NULL,
    updated_at              TIMESTAMP(6),
    deleted_at              TIMESTAMP(6),
    CONSTRAINT ae_character_pk PRIMARY KEY (character_id)
);