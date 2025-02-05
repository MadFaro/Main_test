CREATE TABLE my_table (
    id         SERIAL PRIMARY KEY,
    date_ad    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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
