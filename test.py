WHERE JSON_EXTRACT(marinadb, '$.max_chats_per_operator') IS NOT NULL
  AND JSON_UNQUOTE(JSON_EXTRACT(marinadb, '$.max_chats_per_operator')) != 'null';
