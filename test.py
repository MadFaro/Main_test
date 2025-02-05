query = """
SELECT id as ID,
       datetime_insert as DATE,
       operation_type as TYPE,
       json as JSON,
       login_customer as LOGIN
  FROM operations
  WHERE operation_type = 'Покупка' and status_operation = 'Исполнен'
"""
