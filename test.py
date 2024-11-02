SELECT 
    SUBSTR(ФИО, INSTR(ФИО, ' ') + 1, INSTR(ФИО, ' ', 1, 2) - INSTR(ФИО, ' ') - 1) ||
    ' ' ||
    SUBSTR(ФИО, 1, INSTR(ФИО, ' ') - 1) AS ИФ
FROM 
    таблица;
