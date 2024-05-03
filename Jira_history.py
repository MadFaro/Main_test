' Создание объекта ADO Connection
Set conn = CreateObject("ADODB.Connection")

' Строка подключения к базе данных Oracle
conn.ConnectionString = "Provider=OraOLEDB.Oracle;Data Source=your_datasource;User ID=your_username;Password=your_password"

' Открытие соединения с базой данных
conn.Open

' SQL запрос, который вы хотите выполнить
sqlQuery = "SELECT COUNT(*) AS RecordCount FROM my_table"

' Создание объекта ADO Recordset
Set rs = CreateObject("ADODB.Recordset")

' Выполнение запроса и получение результатов
rs.Open sqlQuery, conn

' Сохранение значения COUNT(*) в переменную
recordCount = rs("RecordCount").Value

' Закрытие объектов Recordset и Connection
rs.Close
conn.Close

' Вывод значения переменной
WScript.Echo "Количество записей в таблице: " & recordCount

