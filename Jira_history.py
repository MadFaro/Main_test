SUBSTR(
           your_column,
           INSTR(your_column, '/*+') + 3,
           INSTR(your_column, '*/') - INSTR(your_column, '/*+') - 3
       ) AS extracted_text
