from os import getenv
from dotenv import load_dotenv

# Token for Bot 
load_dotenv(override=True)
Token = getenv("BOT_TOKEN")

# Admin ids (integer)
admin_ids = []