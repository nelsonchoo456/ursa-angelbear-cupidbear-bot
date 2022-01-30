from dotenv import load_dotenv
import os

load_dotenv()

ANGEL_BOT_TOKEN = os.environ["ANGEL_BOT_TOKEN"]
PLAYERS_FILENAME = os.environ["PLAYERS_FILENAME"]
CHAT_ID_JSON = os.environ["CHAT_ID_JSON"]
ANGEL_ALIAS = os.environ["ANGEL_ALIAS"]
MORTAL_ALIAS = os.environ["MORTAL_ALIAS"]