import pyodbc
import json


class DatabaseInterface:
    
    def __init__(self, server, database, username, password):
        if not hasattr(self, 'cnx'):
            self.cnx = pyodbc.connect('DRIVER=SQL SERVER;SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+password)
            self.cnx.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
            self.cnx.setencoding(encoding='utf-8')
    
    
    def get_cnx(self):
        return self.cnx
    
    def call_proc(self, proc_name, params=None):
        """
        proc: Name of procedure
        params: tuple of parameters
        """
        cnx = self.get_cnx()
        cursor = cnx.cursor()
        if params is None:
            with cnx:
                cursor.execute(f'{proc_name}')
                rows = cursor.fetchall()
                return [row for row in rows]
        else:
            with cnx:
                stored_proc = f"Exec [dbo].[{proc_name}] @id = ?"
                cursor.execute(stored_proc, params)
                rows = cursor.fetchall()
                return [json.loads(row[0]) for row in rows]
