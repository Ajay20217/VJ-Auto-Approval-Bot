# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "11893421"))
    API_HASH = getenv("API_HASH", "f571101b32748bc6f8e2178d03c12dd0")
    BOT_TOKEN = getenv("BOT_TOKEN", "6916331007:AAGhWSWkrA-ht47oFtJF16DVYri4l1epUM0")
    FSUB = getenv("FSUB", "omglinksofficial")
    CHID = int(getenv("CHID", "-1001635195087"))
    SUDO = list(map(int, getenv("SUDO", "6036497605").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://umpiremovie:sYc77AAESIugtrQV@cluster0.lpdoczo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
