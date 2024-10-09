CREATE TABLE buddies (
	buddy_id            VARCHAR(10) NOT NULL,
    character_id        VARCHAR(10),
    get_path            VARCHAR(20),
    seesaa_url          VARCHAR(500),
    aewiki_url          VARCHAR(500),
    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP,
    deleted_at          TIMESTAMP,
    CONSTRAINT ae_buddy_pk PRIMARY KEY (buddy_id)
);