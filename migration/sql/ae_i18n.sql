CREATE TABLE ae_i18n (
    key                 VARCHAR(50) NOT NULL,
    ko                  VARCHAR(500) NOT NULL,
    en                  VARCHAR(500) NOT NULL,
    ja                  VARCHAR(500) NOT NULL,
    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP,
    deleted_at          TIMESTAMP,
    CONSTRAINT ae_i18n_pk PRIMARY KEY (key)
);