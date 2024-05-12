SELECT SUBSTR(dump_result, INSTR(dump_result, ':') + 2, INSTR(dump_result, ',') - INSTR(dump_result, ':') - 2) AS first_code
FROM your_table;
