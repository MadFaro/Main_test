from sqlalchemy.types import Integer, String, Date

data_type = {
    'threadid': Integer,
    'operatorfullname': String(1500),
    'operatorid': Integer,
    'created': Date,
    'modified': Date,
    'state': String(1500),
    'offline': Integer,
    'category': String(1500),
    'subcategory': String(1500),
    'threadkind': String(1500)
}
