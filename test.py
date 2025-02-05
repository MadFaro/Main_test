CREATE TABLE users (
    "index"    SERIAL PRIMARY KEY,
    pass       TEXT,
    sdep       TEXT,
    login      TEXT,
    fio        TEXT,
    status     INTEGER,
    gender     TEXT,
    birth_date TIMESTAMP
);
