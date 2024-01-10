from dotenv import load_dotenv # pip install python-dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID').split(', ')
CHANNEL_ID = os.getenv('CHANNEL_ID', '-1001275637856').split(', ')
# print(CHANNEL_ID)