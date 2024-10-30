from fastapi import APIRouter
from models import Game
from database import mongo_client

router = APIRouter()

@router.post("/")
async def create_game(game: Game):
    await mongo_client['kadi_tidi']['games'].insert_one(game.dict())
    return {"message": "Game created", "game_id": game.id}

@router.get("/{game_id}")
async def get_game(game_id: str):
    game = await mongo_client['kadi_tidi']['games'].find_one({"id": game_id})
    return game
