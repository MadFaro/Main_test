WITH RECURSIVE
json_data(id, datetime_insert, operation_type, json, login_customer, value_operation, status_operation, idx, product_id, count) AS (
    -- Начальный запрос: извлечение первого элемента
    SELECT
        id,
        datetime_insert,
        operation_type,
        json,
        login_customer,
        value_operation,
        status_operation,
        0 AS idx, -- Индекс элемента в массиве
        json_extract(json, '$[0].product_id') AS product_id,
        json_extract(json, '$[0].count') AS count
    FROM
        operations
    WHERE
        json_extract(json, '$[0].product_id') IS NOT NULL

    UNION ALL

    -- Рекурсивный запрос: извлечение последующих элементов
    SELECT
        id,
        datetime_insert,
        operation_type,
        json,
        login_customer,
        value_operation,
        status_operation,
        idx + 1,
        json_extract(json, printf('$[%d].product_id', idx + 1)) AS product_id,
        json_extract(json, printf('$[%d].count', idx + 1)) AS count
    FROM
        json_data
    WHERE
        json_extract(json, printf('$[%d].product_id', idx + 1)) IS NOT NULL
        AND idx < 4  -- Чтобы ограничить количество элементов (0-4 = до 5 элементов)
)

SELECT
    id,
    datetime_insert,
    operation_type,
    json,
    login_customer,
    value_operation,
    status_operation,
    product_id,
    count
FROM
    json_data;
