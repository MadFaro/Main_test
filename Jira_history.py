SUBSTR(
           your_column,
           INSTR(your_column, 'parallel') + LENGTH('parallel'),
           4
       ) AS extracted_text
