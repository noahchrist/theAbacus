from fastapi import APIRouter, HTTPException
from typing import List
from models.market import MarketComparison
from utils.edge_calculator import calculate_edge

router = APIRouter()

@router.get("/markets", response_model=List[MarketComparison])
async def get_markets():
    """Fetch and compare markets from Kalshi and Pinnacle"""
    # TODO: Implement actual fetching logic
    return []

@router.get("/markets/{market_id}")
async def get_market(market_id: str):
    """Get specific market comparison"""
    # TODO: Implement
    return {"market_id": market_id}

@router.post("/calculate-edge")
async def calculate_market_edge(data: dict):
    """Calculate edge for given market data"""
    try:
        edge = calculate_edge(
            kalshi_ask=data['kalshi_ask'],
            pinnacle_over=data['pinnacle_over'],
            pinnacle_under=data['pinnacle_under']
        )
        return {"edge": edge}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))