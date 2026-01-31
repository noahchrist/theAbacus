import os
from dotenv import load_dotenv

load_dotenv()

# Kalshi API Configuration
KALSHI_API_KEY_ID = os.getenv("KALSHI_API_KEY_ID")
KALSHI_API_PRIVATE_KEY = os.getenv("KALSHI_API_PRIVATE_KEY")  # Read key directly from env

# The Odds API
THE_ODDS_API_KEY = os.getenv("THE_ODDS_API_KEY")

# Trading Configuration
EDGE_THRESHOLD = 0.05  # 5% minimum edge
UPDATE_INTERVAL = 300  # seconds between updates