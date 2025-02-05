SELECT setval('table_name_column_name_seq', (SELECT MAX(id) FROM table_name));
