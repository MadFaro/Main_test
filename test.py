select tablespace_name, file_name, bytes/1024/1024 as size_mb
from dba_data_files
where tablespace_name = 'UNDOTBS1';
