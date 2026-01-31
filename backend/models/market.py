from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MarketComparison(BaseModel):
    id: str
    sport: str
    market_type: str
    line: float
    kalshi_ask: float
    kalshi_bid: Optional[float]
    pinnacle_over: float
    pinnacle_under: float
    pinnacle_fair: float
    edge: float
    timestamp: datetime

class EdgeCalculation(BaseModel):
    kalshi_price: float
    pinnacle_fair: float
    edge: float
    ev_per_dollar: float