SELECT id,
       date_ad,
       fio,
       login,
       phone,
       category,
       city,
       name,
       text_ad,
       file_ad,
       moderation
  FROM advt
 WHERE date_ad >= DATE('now', '-30 days');
