# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "9634153"))
    API_HASH = getenv("API_HASH", "67bd6a23278a884e575a6ebf15b0e6bc")
    BOT_TOKEN = getenv("BOT_TOKEN", "6664635995:AAFS1suOi1wQb8CyoiwcNWvQB6D3RBZmRs4")
    FSUB = getenv("FSUB", "NMOAdda")
    CHID = int(getenv("CHID", "--1001732268000"))
    SUDO = list(map(int, getenv("SUDO", "6402835574").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://nivasshetty46:AmuQSnZPzWzbPIBS@cluster0.kz11jeq.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
