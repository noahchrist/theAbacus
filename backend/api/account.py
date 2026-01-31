from fastapi import APIRouter, HTTPException
from utils.kalshi_client import KalshiClient
from config import KALSHI_API_KEY_ID, KALSHI_API_PRIVATE_KEY

router = APIRouter()

# Initialize Kalshi client
kalshi = None
kalshi_error = None

try:
    # Check if keys are configured
    if not KALSHI_API_KEY_ID or not KALSHI_API_PRIVATE_KEY:
        kalshi_error = "Kalshi API keys not configured. Please add KALSHI_API_KEY_ID and KALSHI_API_PRIVATE_KEY to .env"
    else:
        kalshi = KalshiClient(
            api_key_id=KALSHI_API_KEY_ID,
            private_key_str=KALSHI_API_PRIVATE_KEY,
        )
except Exception as e:
    kalshi_error = f"Could not initialize Kalshi client: {str(e)}"
    print(f"Warning: {kalshi_error}")

@router.get("/balance")
async def get_balance():
    """Get Kalshi account balance"""
    if kalshi_error:
        return {
            "balance": "0.00",
            "configured": False,
            "error": kalshi_error
        }
    
    if not kalshi:
        raise HTTPException(status_code=500, detail="Kalshi client not configured")
    
    try:
        balance = kalshi.get_balance()
        return {
            **balance,
            "configured": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/portfolio")
async def get_portfolio():
    """Get Kalshi portfolio positions"""
    if not kalshi:
        raise HTTPException(status_code=500, detail="Kalshi client not configured")
    
    try:
        portfolio = kalshi.get_portfolio()
        return portfolio
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))