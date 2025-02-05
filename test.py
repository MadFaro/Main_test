CREATE TABLE "" (
    id         INTEGER  PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                        UNIQUE ON CONFLICT ROLLBACK
                        NOT NULL,
    date_ad    DATETIME DEFAULT (DATETIME() ),
    fio        TEXT,
    login      TEXT,
    phone      TEXT,
    category   TEXT,
    city       TEXT,
    name       TEXT,
    text_ad    TEXT,
    file_ad    TEXT,
    moderation INTEGER
);

