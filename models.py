from pydantic import BaseModel
from typing import List, Optional

class Card(BaseModel):
    suit: str
    rank: str

class Player(BaseModel):
    id: str
    name: str
    hand: List[Card]

class Game(BaseModel):
    id: str
    players: List[Player]
    deck: List[Card]
    current_turn: Optional[str]
