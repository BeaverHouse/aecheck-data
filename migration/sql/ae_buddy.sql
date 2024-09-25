CREATE TABLE ae_buddy (
	buddy_id            VARCHAR2(10) NOT NULL,
    character_id        VARCHAR2(10),
    get_path            VARCHAR2(20) NOT NULL,
    seesaa_url          VARCHAR2(500),
    aewiki_url          VARCHAR2(500),
    CONSTRAINT ae_buddy_pk PRIMARY KEY (buddy_id)
);