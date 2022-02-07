import redis
import config

rdb = redis.Redis.from_url(config.REDISCLOUD, decode_responses=True)

def set_chatid(playername: str, chat_id: str):
	playername = playername.lower()
	rdb.set(f'chatid:{playername}', chat_id)

def get_chatid(playername: str):
	playername = playername.lower()
	return rdb.get(f'chatid:{playername}')