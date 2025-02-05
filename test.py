SELECT 
    datetime_insert, 
    operation_type, 
    value_operation
FROM operations
WHERE login_customer = 'TOLOGONOVAB@URALSIB.RU'
  AND datetime_insert = (
        SELECT MAX(datetime_insert)
        FROM operations 
        WHERE login_customer = 'TOLOGONOVAB@URALSIB.RU'
    );
