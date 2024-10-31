select 
    threadid, -- ID чата
    operatorfullname, -- ФИО Оператора
    operatorid, -- ID Оператора
    created, -- Дата создания чата
    modified, -- Дата последнего изменения чата
    state, -- Статус
    offline, -- Флаг что чат обработа онлайн
    category, -- Категория
    subcategory, -- Под категория
    threadkind -- Тип чата
    from chatthread where created >= date(now());
