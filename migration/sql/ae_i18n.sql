CREATE TABLE ae_i18n (
    key                 VARCHAR2(50) NOT NULL,
    ko                  VARCHAR2(500) NOT NULL,
    en                  VARCHAR2(500) NOT NULL,
    ja                  VARCHAR2(500) NOT NULL,
    created_at          TIMESTAMP(6) NOT NULL,
    updated_at          TIMESTAMP(6),
    deleted_at          TIMESTAMP(6),
    CONSTRAINT ae_i18n_pk PRIMARY KEY (key)
);