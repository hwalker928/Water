"""
Water
~~~~~~~
Database written in Python

"""
import os
import datetime
import glob
import shutil
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



class River: # Tables
    async def create(db,table_name):
        path = f"data/flows/{db}/rivers/{table_name}"
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except:
                raise Exception("Could not create river! Is a folder missing?")
        else:
            raise Exception("River already exists!")
    
    async def remove(db,table_name):
        path = f"data/flows/{db}/rivers/{table_name}"
        if not os.path.exists(path):
            raise Exception("River not found!")
        else:
            try:
                os.rmdir(path)
            except:
                raise Exception("Could not remove river! Is a folder missing?")

class Drops: # Uhh, dunno
    async def set(key:str,value:str,flow:str,table:str):
        path = f"data/flows/{flow}/rivers/{table}"
        try:
            with open(path+f"/{key}.water","w") as file:
                file.write(str(value))
                file.close()
                if debug:
                    print(f"{debug_text}: Created Drop")
        except:
            raise Exception("Could not create drop! Is a folder missing?")
    
    async def get(key,flow,table):
        path = f"data/flows/{flow}/rivers/{table}"
        try:
            with open(path+f"/{key}.water","r") as file:
                data = file.read()
                return str(data)
        except Exception as e:
            print("This mf : ",e)
            raise Exception("Could not get drop! Is a folder missing?")

    async def delete(key,flow,table):
        try:
            path = f"data/flows/{flow}/rivers/{table}/{key}.water"
            os.remove(path)
            if debug:
                print(f"{debug_text}: Removed Drop")
        except:
            raise Exception("Could not delete drop! Is a folder missing?")

class Flows:# Databases
    async def create(name):
        path = f"data/flows/{name}"
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                tables = f"data/flows/{name}/rivers"
                os.mkdir(tables)
                with open(path+"/info.water", "w") as file:
                    file.write(f"Created at {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.close()
                if debug:
                    print(f"{debug_text}: Flow has been created!")
            else:
                raise Exception("Flow already exists!")
        except:
            raise Exception("Could not create Flow! Is a folder missing?")
        
    async def ls_rivers(db_name:str):
        try:
            old = glob.glob(f"data/flows/{db_name}/rivers/*")
            folders = []
            for folder in old:
                folder = folder.replace(f"data/flows/{db_name}/rivers","")
                folder = folder.replace(f"""\\""","")
                folders.append(folder)
            rivers = folders
            return rivers
        except:
            raise Exception("Could not list rivers! Is a folder missing?")
    
    async def remove(flow):
        try:
            path = f"data/flows/{flow}"
            if not os.path.exists(path):
                raise Exception("Flow not found!")
            else:
                shutil.rmtree(path)
                if debug:
                    print(f"{debug_text}: Flow has been dropped!")  
        except:
            raise Exception("Could not remove River! Is a folder missing?")