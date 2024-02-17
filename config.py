import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23182335")

API_HASH = os.environ.get("API_HASH", "373389a98695c20b5e52084cc636efdf")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6595799324:AAGMXTwqZgt6dhRpBxfGKapouFgJIyo3Z5M") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://shortenerlink95:LYy4CcEnUw6mHw5L@cluster0.gamfmbp.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/b3125068739885e7109db.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
