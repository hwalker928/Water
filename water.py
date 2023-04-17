"""
Water
~~~~~~~
Database written in Python

"""
import os
import datetime
import glob
from cryptography.fernet import Fernet


global debug
debug = True
debug_text = "Water Debugger"

def init():
    global key
    key_is = False
    
    try:
        file = open("data/key.water", "r")
        key = file.read().encode("utf-8")
        key_is = True
    except:
        try:
            file = open("data/key.water", "w")
        except:
            raise Exception("'data' Folder not found!")
    
    if key_is == False:
        key = Fernet.generate_key()
        file.write(key.decode("utf-8"))
    
    global crpytography
    crpytography = Fernet(key)        
    file.close()

def show_debug(state:bool):
    global debug
    debug = bool(state)
    if debug:
        print(f"{debug_text}: Debug mode has been activated!")
    

class Flow:
    class Tables:
        def create(db,table_name):
            path = f"data/databases/{db}/tables/{table_name}"
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                raise Exception("Table already exists!")
        
        def remove(db,table_name):
            path = f"data/databases/{db}/tables/{table_name}"
            if not os.path.exists(path):
                raise Exception("Table not found!")
            else:
                os.rmdir(path)
    
    class Drops:
        def set(key:str,value:str,database:str,table:str):
            path = f"data/databases/{database}/tables/{table}"
            with open(path+f"/{key}.water","w") as file:
                file.write(str(value))
                file.close()
                if debug:
                    print(f"{debug_text}: Created Drop")

        def get(key,database,table):
            path = f"data/databases/{database}/tables/{table}"
            with open(path+f"/{key}.water","r") as file:
                data = file.read()
                return str(data)
    
    class Databases:
        def create(name):
            path = f"data/databases/{name}"
            if not os.path.exists(path):
                os.mkdir(path)
                tables = f"data/databases/{name}/tables"
                os.mkdir(tables)
                with open(path+"/info.water", "w") as file:
                    file.write(f"Created at {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.close()
                if debug:
                    print(f"{debug_text}: Database has been created!")
            else:
                raise Exception("Database already exists!")
        
        def ls_tables(db_name:str):
            old = glob.glob(f"data/databases/{db_name}/tables/*")
            folders = []
            for folder in old:
                folder = folder.replace(f"data/databases/{db_name}/tables","")
                folder = folder.replace(f"""\\""","")
                folders.append(folder)
            tables = folders
            return tables

        def remove(name):
            path = f"data/databases/{name}"
            if not os.path.exists(path):
                raise Exception("Database not found!")
            else:
                os.rmdir(path)
                if debug:
                    print(f"{debug_text}: Database has been dropped!")