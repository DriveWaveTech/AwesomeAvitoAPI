from dotenv import dotenv_values


config = dotenv_values(".env")

ITEM_IDS = config.get("ITEM_IDS")
CHAT_ID = config.get("CHAT_ID")
VOICE_IDS = config.get("VOICE_IDS")
CHATS_V2_IDS = config.get("CHATS_V2_IDS")