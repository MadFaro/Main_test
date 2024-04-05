SELECT JSON_VALUE(your_json_column, '$.config.max_chats_per_operator') AS max_chats_per_operator
FROM your_table;
