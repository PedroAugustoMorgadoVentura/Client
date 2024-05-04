SQL_CREATE_TABLE_CLIENT = """
    CREATE TABLE IF NOT EXISTS client(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone INTEGER NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    password TEXT NOT NULL)
"""

SQL_INSERT_CLIENT = """
    INSERT INTO client(name, phone, email, address, password)
    values (?,?,?,?,?)
    """


SQL_UPDATE_CLIENT = """
    UPDATE client
    SET name= ?, phone= ?, email= ?, address= ? ,password= ?
    Where id = ?
"""

SQL_GET_ALL_CLIENT = """
    SELECT id, name, phone, email, address, password 
    FROM client 
    ORDER by name
"""

SQL_DELETE_CLIENT = """
    DELETE FROM client
    WHERE id=?
"""

SQL_GET_ONE_CLIENT = """
    SELECT id, name, phone, email, address, password 
    FROM client
    WHERE id=?
"""
SQL_GET_COUNT_CLIENT = """
    SELECT COUNT(*) FROM client
"""

