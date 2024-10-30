from motor.motor_asyncio import AsyncIOMotorClient

mongo_client = None

async def connect_to_mongo():
    global mongo_client
    mongo_client = AsyncIOMotorClient('mongodb://localhost:27017')

async def close_mongo_connection():
    global mongo_client
    mongo_client.close()
