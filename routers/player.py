from fastapi import APIRouter
from models import Player
from database import mongo_client

router = APIRouter()

@router.post("/")
async def create_player(player: Player):
    await mongo_client['kadi_tidi']['players'].insert_one(player.dict())
    return {"message": "Player created", "player_id": player.id}

@router.get("/{player_id}")
async def get_player(player_id: str):
    player = await mongo_client['kadi_tidi']['players'].find_one({"id": player_id})
    return player
