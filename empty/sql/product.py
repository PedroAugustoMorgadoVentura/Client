SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT NOT NULL)"""


SQL_INSERT = """
    INSERT INTO product(name, price, description)
    VALUES(?, ?, ?)"""


SQL_GET_ALL = """
    SELECT id, name, price, description
    FROM product
    ORDER by name
"""

SQL_UPDATE = """
    UPDATE product
    SET name= ?, price= ?,description= ?
    WHERE ID = ?
    """

SQL_DELETE = """
    DELETE FROM product
    Where id=?
"""

SQL_GET_ONE = """
    SELECT id, name, price, description
    FROM product
    WHERE id=? 
"""

SQL_GET_COUNT = """
    SELECT COUNT(*) FROM product"""