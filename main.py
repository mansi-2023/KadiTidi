from fastapi import FastAPI
from routers import game, player
from database import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(game.router, prefix="/game")
app.include_router(player.router, prefix="/player")
