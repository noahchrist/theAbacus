import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
KALSHI_API_KEY = os.getenv("KALSHI_API_KEY")
THE_ODDS_API_KEY = os.getenv("THE_ODDS_API_KEY")

# Configuration
EDGE_THRESHOLD = 0.05  # 5% minimum edge
UPDATE_INTERVAL = 300  # seconds between updates
