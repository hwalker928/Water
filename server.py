from fastapi import FastAPI, Request
import asyncio
import water
import os
water.init()
passwd = os.environ.get('WATER_PASSWORD')
app = FastAPI()



@app.get('/')
async def index():
    return str("This is your Server! Have fun with it!")

@app.post("/flows/create")
async def create_flow(request: Request):
    json_data = await request.json()
    if json_data["password"] == passwd:
        try:
            str(await water.Flows.create(json_data["name"]))
            return "Created Flow!"
        except:
            return "Error creating flow!"
    else:
        return "Wrong Password!"
    
@app.post("/flows/delete")
async def delete_flow(request: Request):
    json_data = await request.json()
    if json_data["password"] == passwd:
        try:
            str(await water.Flows.remove(json_data["flow"]))
            return "Deleted Flow!"
        except:
            return "Error deleting flow!"
    else:
        return "Wrong Password!"
    
@app.get("/flows/rivers")
async def list_rivers(request: Request):
    json_data = await request.json()
    if json_data["password"] == passwd:
        try:
            return str(await water.Flows.ls_rivers(json_data["name"]))
        except:
            return "Error listing flows!"
    else:
        return "Wrong Password!"

# Rivers
@app.post("/rivers/create")
async def create_river(request: Request):
    json_data = await request.json()
    if json_data["password"] == passwd:
        try:
            str(await water.River.create(json_data["flow"],json_data["name"]))
            return "Created River"
        except:
            return "Error Creating River!"
    else:
        return "Wrong Password!"

@app.post("/rivers/delete")
async def delete_river(request: Request):
    json_data = await request.json()
    if json_data["password"] == passwd:
        try:
            str(await water.River.remove(json_data["flow"],json_data["river"]))
            return "Deleted River"
        except:
            return "Error deleting River!"
    else:
        return "Wrong Password!"
    
# Drops
@app.post("/drops/delete")
async def delete_drops(request: Request):
    json_data = await request.json()
    if json_data["password"] == passwd:
        try:
            str(await water.Drops.delete(key=json_data["key"],flow=json_data["flow"],table=json_data["river"]))
            return "Deleted Drop!"
        except:
            return "Error deleting River!"
    else:
        return "Wrong Password!"

@app.post("/drops/create")
async def create_drop(request: Request):
    json_data = await request.json()
    if json_data["password"] == passwd:
        try:
            str(await water.Drops.set(json_data["key"],json_data["value"],json_data["flow"],json_data["river"]))
            return "Created Drop!"
        except:
            return "Error creating Drop!"
    else:
        return "Wrong Password!"

@app.get("/drops/get")
async def get_drop(request: Request):
    json_data = await request.json()
    if json_data["password"] == passwd:
        try:
            return str(await water.Drops.get(json_data["key"],json_data["flow"],json_data["river"]))
        except:
            return "Error getting Drop!"
    else:
        return "Wrong Password!"