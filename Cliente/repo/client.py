import sqlite3
from typing import List, Optional
from models.client import Client
from sql.client import *
from util.database import create_connection



class ClientRepo:
    def create_table_client(cls) -> bool:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_CREATE_TABLE_CLIENT)
                return True
        except sqlite3.Error as ex:
            print(ex)
            return False
    @classmethod
    def insert_client(cls, client: Client) -> Optional[Client]:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_INSERT_CLIENT,( 
                               client.name, 
                               client.phone, 
                               client.email, 
                               client.address, 
                               client.password))
                if cursor.rowcount > 0:
                    client.id = cursor.lastrowid
                    return client

        except sqlite3.Error as ex:
            print(ex)
            return None
        
    @classmethod
    def get_all_client(cls) ->List[Client]:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                tuples = cursor.execute(SQL_GET_ALL_CLIENT).fetchall()
                clients = [Client(*c) for c in tuples]
                return clients
        except sqlite3.Error as ex:
            print(ex)
            return False
    @classmethod   
    def update_client(cls, client: Client) -> bool:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_UPDATE_CLIENT, (
                               client.name, 
                               client.phone, 
                               client.email, 
                               client.address, 
                               client.password,
                               client.id
                ))
                if cursor.rowcount > 0:
                    client.id = cursor.lastrowid
                    return True
        except sqlite3.Error as ex:
            print(ex)
            return False
        
    @classmethod   
    def delete_client(cls, id: int) -> bool:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(SQL_DELETE_CLIENT, (id,))
                if cursor.rowcount > 0:
                    return True
        except sqlite3.Error as ex:
            print(ex)
            return False
    @classmethod
    def get_one_client(cls, id: int) -> Optional[Client]:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                tuple = cursor.execute(SQL_GET_ONE_CLIENT, (id,)).fetchone() 
                client = Client(*tuple)
                return client
        except sqlite3.Error as ex:
            print(ex)
            return False
    @classmethod
    def get_count(cls) -> Optional[int]:
        try:
            with create_connection() as conn:
                cursor = conn.cursor()
                tuple = cursor.execute(SQL_GET_COUNT_CLIENT).fetchone()
                amount = int(tuple[0])
                return amount
        except sqlite3.Error as ex:
            print(ex)
            return False