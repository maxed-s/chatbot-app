import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
INTUIT_REDIRECT_URL = os.getenv("INTUIT_REDIRECT_URL")
REALM_ID = os.getenv("REALM_ID")
ATUHORIZAION_CODE = os.getenv("ATUHORIZAION_CODE")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

client_secrets = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "redirect_uri": INTUIT_REDIRECT_URL,
    "environment": "sandbox"
}

REALM_ID_INT = int(REALM_ID)

qBooksAssets = {
    "authentication_assets" : {
        "realm_id": REALM_ID_INT,
        "auth_code": ATUHORIZAION_CODE
    }
}

refreshToken = REFRESH_TOKEN

qBData = {
    "realm_id":REALM_ID,
    "accessToken":ACCESS_TOKEN
}