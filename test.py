from sqlalchemy.dialects import oracle
from sqlalchemy.types import VARCHAR, Float

# Определение типов данных для колонок с учетом Oracle
data_type = {
    'MONTH': VARCHAR(50),
    'TABNUM': VARCHAR(50),
    'FIO': VARCHAR(100),
    'PODRAZDELENIE': VARCHAR(50),
    'DOLZHHNOST': VARCHAR(50),
    'STAG': VARCHAR(50),
    'TYPE_CODE': VARCHAR(50),
    'STATUS': VARCHAR(50),
    'DIRECT': VARCHAR(50),
    'SALES': Float(precision=53).with_variant(oracle.FLOAT(binary_precision=126), 'oracle'),
    'ATT': Float(precision=53).with_variant(oracle.FLOAT(binary_precision=126), 'oracle'),
    'CSI': Float(precision=53).with_variant(oracle.FLOAT(binary_precision=126), 'oracle'),
    'SCORE': Float(precision=53).with_variant(oracle.FLOAT(binary_precision=126), 'oracle'),
    'DISCIPLINE': Float(precision=53).with_variant(oracle.FLOAT(binary_precision=126), 'oracle'),
    'EST': Float(precision=53).with_variant(oracle.FLOAT(binary_precision=126), 'oracle'),
    'SUM': Float(precision=53).with_variant(oracle.FLOAT(binary_precision=126), 'oracle')
}
