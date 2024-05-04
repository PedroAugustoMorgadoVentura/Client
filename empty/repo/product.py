import sqlite3
from typing import List, Optional
from models.product import Product
from sql.product import *
from util.database import create_connection



class ProductRepo:

    def create_table(cls) -> bool:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE)
                return True
        except sqlite3.Error as ex:
            print(ex)
            return False
    @classmethod
    def insert(cls, product: Product) -> Optional[Product]:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT, (
                    product.name,
                    product.price,
                    product.description,
                    product.id
                )) #EVERY TIME YOU EXECUTE A SEQUEL COMMAND THAT REQUIRES PARAMETERS, YOU HAVE TO PROVIDE AS A TUPLE
                if cursor.rowcount > 0:
                    product.id = cursor.lastrowid
                    return product
            
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    @classmethod
    def get_all(cls) -> List[Product]:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                tuples = cursor.execute(SQL_GET_ALL).fetchall()
                products = [Product(*t) for t in tuples]
                return products
        except sqlite3.Error as ex:
            print(ex)
            return False
        
    @classmethod
    def update(cls, product: Product) -> bool:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE, (
                    product.name,
                    product.price,
                    product.description,
                    product.id
                )) #EVERY TIME YOU EXECUTE A SEQUEL COMMAND THAT REQUIRES PARAMETERS, YOU HAVE TO PROVIDE AS A TUPLE
                if cursor.rowcount > 0:
                    product.id = cursor.lastrowid
                    return True
            
        except sqlite3.Error as ex:
            print(ex)
            return False
        


    @classmethod
    def delete(cls, id: int) -> bool:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_DELETE, (id,)) #EVERY TIME YOU EXECUTE A SEQUEL COMMAND THAT REQUIRES PARAMETERS, YOU HAVE TO PROVIDE AS A TUPLE
                if cursor.rowcount > 0:
                    return True
            
        except sqlite3.Error as ex:
            print(ex)
            return False
    
    @classmethod
    def get_one(cls, id: int) -> Optional[Product]:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                tuple = cursor.execute(SQL_GET_ONE, (id,)).fetchone() #EVERY TIME YOU EXECUTE A SEQUEL COMMAND THAT REQUIRES PARAMETERS, YOU HAVE TO PROVIDE AS A TUPLE
                product = Product(*tuple)
                return product
        except sqlite3.Error as ex:
            print(ex)
            return False
        


    @classmethod
    def get_count(cls) -> Optional[int]:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                tuple = cursor.execute(SQL_GET_COUNT).fetchone()
                amount = int(tuple[0])
                return amount
        except sqlite3.Error as ex:
            print(ex)
            return False