import os

API_ID = API_ID = 

API_HASH = os.environ.get("API_HASH", "c0d4308321c6703b82a27b0c9966ceaa")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7030512672:AAH_1BOWLHDDMoQAxSwXmiEUCfiDulBz3qs")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6722252412))

LOG = -1001952769436

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6722252412").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


