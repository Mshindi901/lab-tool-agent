import os

from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

heartbeatInterval = int(os.getenv("HEARTBEAT_INTERVAL", 30))
requestTimeout = int(os.getenv("REQUEST_TIMEOUT", 10));

if not API_URL:
    raise RuntimeError("Api Url not provided");